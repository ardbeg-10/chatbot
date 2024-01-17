from langchain.vectorstores.neo4j_vector import Neo4jVector
from llm import embeddings, llm
import streamlit as st

neo4jvector = Neo4jVector.from_existing_index(
    embeddings,                              # (1)
    url=st.secrets["NEO4J_URI"],             # (2)
    username=st.secrets["NEO4J_USERNAME"],   # (3)
    password=st.secrets["NEO4J_PASSWORD"],   # (4)
    index_name="lectureSummary",                 # (5)
    node_label="Lecture",                      # (6)
    text_node_property="Summary",               # (7)
    embedding_node_property="embedding", # (8)
    retrieval_query="""
RETURN
    node.Topic, node.Date, node.Lecture_Id, node.Timestamp, node.Text, node.Summary as text,
    score,
    {
        topic: node.Topic,
        date: node.Date,
        lectureId: node.Lecture_Id,
        timestamp: node.Timestamp,
        summary: node.Summary
    } AS metadata
"""
)

retriever = neo4jvector.as_retriever()

from langchain.chains import RetrievalQA

kg_qa = RetrievalQA.from_chain_type(
    llm,                  # (1)
    chain_type="stuff",   # (2)
    retriever=retriever,  # (3)
)

