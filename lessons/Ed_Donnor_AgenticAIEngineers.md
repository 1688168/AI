# <center><b><span style="color:orange">Agentic AI Engineer</span></b></center>
> # <b><span style="color:purple">Lab1</span></b>
> ### <b><span style="color:green">Env Keys</span></b>

```
.env file

* setup OPENAI_API_KEY
```

```python
# The imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace
# The usual starting point

load_dotenv(override=True) #set override as True
```

> ### <b><span style="color:green">Communicating with LLM</span></b>
* system prompt
* user prompt

> ### <b><span style="color:green">construct the msg and get response</span></b>

```python
messages = [{"role": "user", "content": "What is 2+2?"}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print(response.choices[0].message.content)

```
> another example to raise a question to LLM
```python
openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)
question = response.choices[0].message.content
print(question)
```


```python
# Make an agent with name, instructions, model

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")

# Run the joke with Runner.run(agent, prompt) then print final_output

# start a conversation with trace with LLM
with trace("Telling a joke"):
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)
```
* in lab1, we only ask and does not processing the response
* where to check the trace: https://platform.openai.com/traces

> # <b><span style="color:purple">Lab 2</span></b>
> ### <b><span style="color:green">use openAI interface to call with different LLM model</span></b>

```python
model_name = "gpt-4o-mini"

response = openai.chat.completions.create(model=model_name, messages=messages) # call with different model

answer = response.choices[0].message.content

display(Markdown(answer)) #how to print markdown
competitors.append(model_name)
answers.append(answer)
```
> # <b><span style="color:purple">role content</span></b>

  
```python
# Judgement time!
judge_messages = [{"role": "user", "content": judge}]
openai = OpenAI()
response = openai.chat.completions.create(
    model="o3-mini",
    messages=judge_messages,
)
results = response.choices[0].message.content
print(results)
```

> # <b><span style="color:purple">Lab 3</span></b>

* Resources
  - PDF.pdf
  - summary.txt

* pdfReader: read the pdf
* read the summary
* define system prompt and provide context from pdf+summary.  So this will define the perspective of LLM for the overall conversation.   We, therefore, do not need to redefine the system role in each msg.

> ### <b><span style="color:green">a query with system prompt</span></b>
```python
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content
```


> ### <b><span style="color:green">how to call functions in global scope by look up</span></b>


```python
def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        tool = globals().get(tool_name)
        result = tool(**arguments) if tool else {}
        results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
    return results
```


> ### <b><span style="color:green">Tools</span></b>
* need to update in system prompt when to call what tools
* check response finish_reason, call tools if we got "tool_calls"


> # <b><span style="color:purple">Open AI SDK</span></b>
> ### <b><span style="color:green">Add Trace</span></b>
```python
with trace("Telling a joke"):
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)
```
* [OpenAI - Trace](https://platform.openai.com/traces)

> ### <b><span style="color:green">How to send email in python</span></b>

```python
def send_test_email():
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("ed@edwarddonner.com")  # Change to your verified sender
    to_email = To("ed.donner@gmail.com")  # Change to your recipient
    content = Content("text/plain", "This is an important test email")
    mail = Mail(from_email, to_email, "Test email", content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print(response.status_code)

send_test_email()
```

> # <b><span style="color:purple">Create Agent</span></b>
> ### <b><span style="color:green">stream communicating with created agent</span></b>

```python
sales_agent1 = Agent(
        name="Professional Sales Agent",
        instructions=instructions1,
        model="gpt-4o-mini"
)

sales_agent2 = Agent(
        name="Engaging Sales Agent",
        instructions=instructions2,
        model="gpt-4o-mini"
)

sales_agent3 = Agent(
        name="Busy Sales Agent",
        instructions=instructions3,
        model="gpt-4o-mini"
)

result = Runner.run_streamed(sales_agent1, input="Write a cold sales email")
async for event in result.stream_events():
    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
        print(event.data.delta, end="", flush=True)


message = "Write a cold sales email"

# run queries to openAI in parallel with TRACE
with trace("Parallel cold emails"):
    results = await asyncio.gather(
        Runner.run(sales_agent1, message),
        Runner.run(sales_agent2, message),
        Runner.run(sales_agent3, message),
    )

outputs = [result.final_output for result in results]

for output in outputs:
    print(output + "\n\n")
```
> # <b><span style="color:purple">Tools</span></b>
> ### <b><span style="color:green">convert function to a tool</span></b>
```python
@function_tool
def send_email(body: str):
    """ Send out an email with the given body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("ed@edwarddonner.com")  # Change to your verified sender
    to_email = To("ed.donner@gmail.com")  # Change to your recipient
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, "Sales email", content).get()
    sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}
``

> ### <b><span style="color:green">Convert Agent to a tool</span></b>
```python
tool1 = sales_agent1.as_tool(tool_name="sales_agent1", tool_description="Write a cold sales email")
tool1
```

> # <b><span style="color:purple">create a manager that knows how to use tools</span></span></b>

```python
sales_manager = Agent(name="Sales Manager", instructions=instructions, tools=tools, model="gpt-4o-mini")

message = "Send a cold sales email addressed to 'Dear CEO'"

with trace("Sales manager"):
    result = await Runner.run(sales_manager, message)
```

> # <b><span style="color:purple">Handoffs</span></b>
* tool vs handoff: tools-> control passes back
> ### <b><span style="color:green">example</span></b>

```python
# Improved instructions thanks to student Guillermo F.

sales_manager_instructions = """
You are a Sales Manager at ComplAI. Your goal is to find the single best cold sales email using the sales_agent tools.
 
Follow these steps carefully:
1. Generate Drafts: Use all three sales_agent tools to generate three different email drafts. Do not proceed until all three drafts are ready.
 
2. Evaluate and Select: Review the drafts and choose the single best email using your judgment of which one is most effective.
You can use the tools multiple times if you're not satisfied with the results from the first try.
 
3. Handoff for Sending: Pass ONLY the winning email draft to the 'Email Manager' agent. The Email Manager will take care of formatting and sending.
 
Crucial Rules:
- You must use the sales agent tools to generate the drafts — do not write them yourself.
- You must hand off exactly ONE email to the Email Manager — never more than one.
"""


sales_manager = Agent(
    name="Sales Manager",
    instructions=sales_manager_instructions,
    tools=tools,
    handoffs=handoffs,
    model="gpt-4o-mini")

message = "Send out a cold sales email addressed to Dear CEO from Alice"

with trace("Automated SDR"):
    result = await Runner.run(sales_manager, message)
```

> # <b><span style="color:purple">OpenAI Async</span></b>
> ### <b><span style="color:green">AsyncIO example</span></b>

```python
from dotenv import load_dotenv
from openai import AsyncOpenAI. #<<<<< AsyncOpenAI
from agents import Agent, Runner, trace, function_tool, OpenAIChatCompletionsModel, input_guardrail, GuardrailFunctionOutput
from typing import Dict
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from pydantic import BaseModel
```


> # <b><span style="color:purple">---</span></b>
> ### <b><span style="color:green">---</span></b>
