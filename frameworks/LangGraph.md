# LangGraph
### LangChain/LangGraph/LangSmith
* LangChain ecosystem - chaining LLM calls
  * memory
  * RAG
  * LCEL //langChain's language
* LangGraph - Agentic
  * LangGraph - separate offering
  * can use diff LLMs
  * LangGraph Studio - LangGraph platform
* LangSmith - Observabilitythis 


### Concepts
* State: the current snapshot of the application
* Nodes: python functions that represent agent logic.  Receive the current state as input, do something, and return an updated State.
* Edges: python functions that determine which node to execute next based on the state.  Can be conditional or fixed.   