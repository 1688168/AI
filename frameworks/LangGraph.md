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

### 5 steps to the first graph
1. Define state
2. Start the grap builder
3. Create a node
4. Create Edge
5. Compile the graph

### LangSmith

### Tools - out of the box

### Tools - Custom

### Super-Step
* a single iteration over the graph nodes.

### Memory - Checkpointing