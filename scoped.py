# tag::importtool[]
from langchain.tools import Tool
# end::importtool[]
from langchain.agents import initialize_agent, AgentType
from langchain.agents import ConversationalChatAgent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from solutions.llm import llm

# Use the Chains built in the previous lessons
from solutions.tools.vector import kg_qa
# from solutions.tools.finetuned import cypher_qa
from solutions.tools.fewshot import cypher_qa

# tag::tools[]
tools = [
    Tool.from_function(
        name="Cypher QA",
        description="Provide information about course content questions using Cypher",
        func=cypher_qa,
    ),
    Tool.from_function(
        name="Vector Search Index",
        description="Provides information about lecture summaries using Vector Search",
        func = kg_qa,
    )
]
# end::tools[]


# tag::memory[]
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)
# end::memory[]

# tag::prompt[]
SYSTEM_MESSAGE = """
    You are a tutor in computer systems providing students guidance to learn. Be interactive.

    If a student answers correctly, give an explanation and proceed to the next step.

    If a student answers incorrectly, correct them and be helpful.
"""
# end::prompt[]

# tag::agent[]
agent = initialize_agent(
    tools,
    llm,
    memory=memory,
    verbose=True,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    agent_kwargs={"system_message": SYSTEM_MESSAGE}
)
# end::agent[]


# tag::generate_response[]
def generate_response(prompt):
    """
    Create a handler that calls the Conversational agent
    and returns a response to be rendered in the UI
    """

    response = agent(prompt)

    return response['output']
# end::generate_response[]

