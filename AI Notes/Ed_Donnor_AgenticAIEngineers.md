# <center><b><span style="color:orange">Agentic AI Engineer</span></b></center>

## Resrouces

## Basics
* How to make LLM call via api
* How to parse out the answer
* What is AI Agents: Where LLM outputs controls the workflow.

## Workflow Design Patterns
1. Prompt Chaining
2. Routing
3. Parallelization
4. Orchestrator-worker
5. Evaluator-Optimizer

## LangChain VS LangGraph
## LangGraph
* LangGraph (Framework) --- Crew AI
* LangGraph Studio (visual builder)
* LangGraph platform (Hosted solution)

> components of LangGraph
* Agent workflows
* State - current snapshot
* Node - python functions - do something on state - return new state - task
* Edges - connections connect the node - also python functions - what's the next task

> 5 steps to the first graph
* define the state class
* start the graph builder
* create a node
* create edges
* compile the graph