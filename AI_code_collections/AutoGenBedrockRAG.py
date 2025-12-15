"""
pip install -U "autogen-agentchat" "autogen-ext[anthropic]" sentence-transformers faiss-cpu numpy

Env (AWS creds):
- Standard AWS credential chain works (AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY[/AWS_SESSION_TOKEN],
  or ~/.aws/credentials, or IAM role), plus AWS_REGION.

Docs:
- AutoGen AgentChat quickstart uses AssistantAgent + Console(run_stream) :contentReference[oaicite:1]{index=1}
- AnthropicBedrockChatCompletionClient is the Bedrock LLM client :contentReference[oaicite:2]{index=2}
"""

import os
import glob
import asyncio
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console

from autogen_core.models import ModelInfo
from autogen_ext.models.anthropic import AnthropicBedrockChatCompletionClient, BedrockInfo


# -----------------------------
# Local RAG (embeddings + FAISS)
# -----------------------------
DOCS_DIR = os.environ.get("LOCAL_DOCS_DIR", "./docs")  # folder containing .txt files
CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
TOP_K = 4

embedder = SentenceTransformer("all-MiniLM-L6-v2")
dim = embedder.get_sentence_embedding_dimension()
index = faiss.IndexFlatIP(dim)  # cosine similarity using normalized vectors

chunks: List[str] = []
metas: List[Tuple[str, int]] = []  # (doc_id, chunk_id)

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    text = " ".join(text.split())
    out, start = [], 0
    while start < len(text):
        end = min(len(text), start + chunk_size)
        out.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return out

def build_index() -> None:
    paths = sorted(glob.glob(os.path.join(DOCS_DIR, "*.txt")))
    if not paths:
        raise FileNotFoundError(f"No .txt files found in {DOCS_DIR}. Set LOCAL_DOCS_DIR or add docs.")

    local_chunks, local_metas = [], []
    for p in paths:
        doc_id = os.path.basename(p)
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
        for i, c in enumerate(chunk_text(text, CHUNK_SIZE, CHUNK_OVERLAP)):
            local_chunks.append(c)
            local_metas.append((doc_id, i))

    vecs = embedder.encode(local_chunks, convert_to_numpy=True).astype("float32")
    faiss.normalize_L2(vecs)
    index.add(vecs)

    chunks.extend(local_chunks)
    metas.extend(local_metas)

build_index()

async def retrieve_local(query: str, k: int = TOP_K) -> str:
    """
    Tool for the agent: retrieve top-k chunks from local FAISS index.
    Returns a compact context block with citations like [Doc: file.txt].
    """
    qv = embedder.encode([query], convert_to_numpy=True).astype("float32")
    faiss.normalize_L2(qv)
    scores, ids = index.search(qv, k)

    out = []
    for rank, (idx, score) in enumerate(zip(ids[0].tolist(), scores[0].tolist()), start=1):
        if idx == -1:
            continue
        doc_id, chunk_id = metas[idx]
        out.append(
            f"[Result {rank}] score={score:.3f} [Doc: {doc_id}] (chunk {chunk_id})\n{chunks[idx]}"
        )
    return "\n\n".join(out) if out else "NO_RESULTS"


# -----------------------------
# Bedrock LLM (AutoGen model client)
# -----------------------------
REGION = os.environ.get("AWS_REGION", "us-east-1")

model_client = AnthropicBedrockChatCompletionClient(
    # Use a Bedrock model ID for Claude on Bedrock (example below).
    model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    temperature=0.2,
    # ModelInfo tells AutoGen what the model supports (notably tool calling).
    model_info=ModelInfo(
        vision=False,
        function_calling=True,
        json_output=False,
        structured_output=True,
        family="claude",
    ),
    # BedrockInfo can be minimal (region) if you rely on AWS default credential chain.
    bedrock_info=BedrockInfo(aws_region=REGION),
)

agent = AssistantAgent(
    name="rag_agent",
    model_client=model_client,
    tools=[retrieve_local],  # <- local RAG tool
    system_message=(
        "You are a helpful assistant.\n"
        "If the question could be answered from the local docs, call retrieve_local(query) first.\n"
        "Use the retrieved context to answer, and cite sources as [Doc: <filename>].\n"
        "If the context is insufficient, say so."
    ),
    reflect_on_tool_use=True,
    model_client_stream=True,
)

async def main() -> None:
    # Ask something that should hit your local docs.
    await Console(agent.run_stream(task="Summarize our onboarding steps for Product X."))
    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
