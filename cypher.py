from langchain.chains import GraphCypherQAChain
# tag::import-prompt-template[]
from langchain.prompts.prompt import PromptTemplate
# end::import-prompt-template[]

from llm import llm
from graph import graph

# tag::prompt[]
CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher to answer questions about lecture topics and provide recommendations.
Convert the user's question based on the schema.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Example Cypher Statements:

1. How to find which lecture mentions a Topic:
```

match (l:Lecture)-[:MENTIONS]-(t:Topic{name:"Topic"}) return l.Lecture_Id as lectureThatMentions.


```

Schema:
{schema}

Question:
{question}
"""
# end::prompt[]

# tag::template[]
cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)
# end::template[]


# tag::cypher-qa[]
cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
)
# tag::cypher-qa[]