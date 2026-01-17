# RAG - How to build knowledge

## two types of LLM
* Auto-regressive LLM: predict the next token (the typical LLM you know of)
* auto-encoding: vector encoding. take full input sequence, produce full output
  * sentiment analysis
  * vector embeddings: representing an input as a list of numbers. ie. a vector
  * token vs vector
  * token is input, vector is output
  * map words to token (input in another form)
  * vector try to create relation of some sort of context
  * vector is the meaning of token
  * embedding: transformer representation
  * king - men + women -> queen
  * paris - france + England -> London
  * cosin similarity
  * sementic search

> `How vector represent meaning?`
* could have thousands of dimensions
* presendt an understanding of the input.  similar inputs are close to each other
? how to map token to vector, identify the meaning?
* NLP: pre-transformer

## what is RAG, Big Idea about RAG
* what's the ticket price to Hethrew?
  * covnert the text into vector
  * find all similar vector around vector -> vector store?  all the information near the input? -> those are the fuzzy look up -> additional context appended
  * encoder LLM has nothing to do with LLM. encoder LLM is just used to look upl vector store.
  * finding relevant content.  contents of similar meaning


## LangChain, Vectors, Chroma
* 2025 Oct V1 ( original Oct 2022)
> pros & Cons
** pros **
* faster time to market
* common in enterprise. good resume material
** cons **
* all the provider has openAI API. less need for this abstraction layer
* light weight, now is heavy weight
* learning curve
* it has it's own language
* liteLLM now is available

> langGraph VS LangChain
> vector database: Chroma (vector was created by encoder LLM)
* it matters more on accuracy on encoder (the energy should focus on this)
* vectorstores are mainly infra or cost concerns


## 10 RAG Advanced Techniques
* Chunking R&D
* Encoder R&D
* Improve Prompts
* Document pre-processing, convert the original document be more vector friendly before convert
* Query rewriting: rewrite the query so it can be more RAG friendly before submitting to LLM
* Query expansion: use LLM to turn the questions into multiple RAG query
* Re-ranking: use an LLM to sub-select from RAG results
* Hierarchical: use an LLM to summarize at multiple levels
* Graph RAG: retrieve content closely related to similar documents
* Agentic RAG: use Agents for retrieval, combining with memory and tools such as SQL