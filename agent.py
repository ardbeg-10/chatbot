from langchain.agents import AgentType, initialize_agent
from langchain.chains import GraphCypherQAChain
from llm import llm

from langchain.chains.conversation.memory import ConversationBufferWindowMemory

from langchain.tools import Tool

from langchain.tools import Tool

from tools.vector import kg_qa

from graph import graph

from tools.cypher import cypher_qa

SYSTEM_MESSAGE = """
You are a course assistant providing information about lectures and topics.
Be as helpful as possible and return as much information as possible.
When the user wants to explore a topic, you should always provide the lecture that mentions it, itsdate, timestamp, and summary.

If a student tells you that they missed a lecture, try to conjecture the lectureID and use vector search index to find more information. you should provide them with the lecture date, the topic mentioned, and summary.

Do not answer any questions using your pre-trained knowledge, only use the information provided in the context.
"""

tools = [
    Tool.from_function(
        name="Vector Search Index", 
        description="Provides information about lectures using Vector Search.", 
        func = kg_qa, 
    ), 
]

# tag::memory[]
memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True,
)
# end::memory[]

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


"""

The `generate_response()` method can be called from the `handle_submit()` method in `bot.py`:

# tag::import[]
from agent import generate_response
# end::import[]

# tag::submit[]
# Submit handler
def handle_submit(message):
    # Handle the response
    with st.spinner('Thinking...'):

        response = generate_response(message)
        write_message('assistant', response)
# end::submit[]

"""
