### Amazon Bedrock Agents
* integrate with knowledge
  * agent -> edit in agent builder -> knowledge -> add -> select knowledge base.
* "prepare" the agent each time you modify the agent


### Create RAG - knowledge base
* create knowledge base -> cannot create as root user

* create S3 to host documents (knowledge)
* upload pdf to S3 (raw data for knowledge)
* bedrock->builder tools -> knowledge bases -> create -> knowledge base with vector store.
* Knowledge -> IAM permissions (need access S3 or other services)


### Create Lambda function the agent can invoke
* use openAI schema


### OpenAPISchema
* edit Agent Builder ->