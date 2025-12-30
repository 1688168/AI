# LLM Engineering - RAG, OloRA, Agents

### Resources
* [Course Homepage](https://edwarddonner.com/2024/11/13/llm-engineering-resources/)
* [Course Slides](https://drive.google.com/drive/folders/1JwNorpRHdnf_pU0GE5yYtfKlyrKC3CoV)
* [Github - Ed Donner - LLM Engineering](https://github.com/ed-donner/llm_engineering)
* [Claude - Cookbook](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/basic_workflows.ipynb)
* [ollama](https://ollama.com/)

### Environments
* Setup Ollama
* UV
  * uv self update #to update uv
  * uv sync #this is like pip install -r requirements.txt

### Play with Ollama
* ollama
* ollama serve
* ollama run gemma3:270m #how to run an open source. model locally?
* ollama pull <model_name>
* ollama ls # list all tghe models you have downloaded
* ollama rm <model_name>
* CTRL+D # to end the gemma session

ex:
- !ollama serve
- !ollama pull llama3.2
- !ollama pull gpt-oss:20b

## Lectures
## Sec1: chat completion API

### Sec1/Day1
* how to add virtual env to vscode search path?
  * go to settings->vscode setting->search venv->add the path to search list
* how to make API call to OpenAI
### Sec1/Day2
* how to use openAI SDK interface call diff LLM providers
* How to call LLM via OLLOMA locally

### SEC1/Day3: LLMs in 3 Flavors
* Base Model -> predict next token - train new skill
* Chat/Instruct-(assistant prompt/user prompt) - better for interactive use cases
* Reasoning/Thinking: chain-of-thought prompting: (think step-by-step to force GPT perform better)
  * reasoning budget. (budget forcing ---- adding wait). always better on puzzle
* Hybrid

### SEC1/Day4
* convert words to toekn and decode
* illusion of "memory": always pass the whole convo history to the chat for memory
* multi-shot prompt

### RAG
* use blob load read all pdf. parse file name as key into text of pdf body as content as simple memory lookup. append to context to LLM
* Fake RAG cannot handle fuzzy matching. The matched key might not relevent in the context. different ppl might have same last name.  So using only last name as key look up content actual is misleading.

### `Vector`
* two flavors of LLM: 
  * auto-regressive LLM predict a future token from the past
  * auto-encoding LLM produce output based on the full input (classification. sentiment analysis, calculate "Vector Embeddings")

### Fine-Tuning frontier model
* Generalization: The ability of a model to make good predictions on unseen data
* Transfer Learning (Fine-Tune)

### Capstone project
> Price prediction
* Regression model (traditional form of AI)

### Parameters (Training)
* forward pass: raw data -> predict
* Loss: how far off was it
* Backward pass: wiggle the parameters (backpropagation, backprop)
* Optimization: take a step in the right direction

### Huggingface
