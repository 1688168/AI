# MCP
### What is MCP
* a protocol
* a simple way to integrate tools, resources, prompts.
* It's more about the ecosystem
* MCP is about sharing tool

### 3 core concepts of MCP
* HOST: An LLM App
* MCP Client: lives inside host and connects 1:1 to MCP Server
* MCP Server: provides tools, context and prompts
![](../Codes/rcs/mcp501.png)

### two transport mechanism
* stdio (Local)
* SSE (HTTPS) - server side event: for remote MCP Servier