import streamlit as st
from utils import write_message
from agent import generate_response

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm the CSO Course Assistant Chatbot! You can ask me anything about the course and content mentioned in lectures as well as recitations. How can I help you?"},
    ]

def handle_submit(message):
    # Handle the response
    with st.spinner('Thinking...'):

        response = generate_response(message)
        write_message('assistant', response)

with st.container():
    # Display messages in Session State
    for message in st.session_state.messages:
        write_message(message['role'], message['content'], save=False)

    # Handle any user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        write_message('user', prompt)

        # Generate a response
        handle_submit(prompt) 
