import streamlit as st
import requests
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# LM Studio API configuration
API_BASE = "http://localhost:1234/v1"  # LM Studio API URL
MODEL_NAME = "llama-3.2-1b"  # Change if using another model

# Initialize LangChain with LM Studio
llm = ChatOpenAI(
    model=MODEL_NAME,
    openai_api_base=API_BASE,
    openai_api_key="lm-studio",  # Dummy key (not used but required)
)

# Streamlit UI
st.title("🤖 AI Chatbot (LangChain + LM Studio)")

# Store messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response using LangChain + LM Studio
    response = llm.invoke([HumanMessage(content=user_input)])

    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response.content)
