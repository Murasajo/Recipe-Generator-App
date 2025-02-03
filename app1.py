import streamlit as st
import os
import json
from langchain_groq import ChatGroq
from langchain_community.document_loaders import JSONLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page settings
st.set_page_config(
    page_title="Recipe Generator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .main-container {
        text-align: center;
        padding: 0.35rem;
        background-color: #E69B55;
        border-radius: 25px;
        margin: 4rem auto;
        width: 100%;
    }
    .chat-container {
        max-width: 800px;
        margin: 20px auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .message {
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        align-items: flex-end;
    }
    .bot-message {
        align-items: flex-start;
    }
    .message-bubble {
        max-width: 70%;
        padding: 12px 16px;
        border-radius: 16px;
        margin: 4px 0;
        font-size: 15px;
        line-height: 1.5;
        word-wrap: break-word;
    }
    .user-bubble {
        background: #E69B55;
        color: white;
        border-radius: 16px 16px 4px 16px;
    }
    .bot-bubble {
        background: #f0f2f5;
        color: #1a1a1a;
        border-radius: 16px 16px 16px 4px;
    }
    
    .stButton > button {
        background-color: #E69B55;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        border: none;
        font-size: 1.1rem;
    }
    .title {
        color: #E69B55;
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .contributors {
        position: fixed;
        bottom: 20px;
        width: 100%;
        text-align: center;
        color: #666;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

if "vector" not in st.session_state:
    st.session_state.embeddings = OpenAIEmbeddings()
    st.session_state.json_loader = JSONLoader(
        file_path="scraped_recipes.json",
        jq_schema=".[]",
        text_content=False
    )
    st.session_state.docs = st.session_state.json_loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:100])
    st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

def switch_to_chat():
    st.session_state.page = 'chat'

def home_page():
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.markdown('<h1 style="color: #E69B55; font-size: 4rem;">Recipe Generator</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.2rem;">Enter your ingredients to discover recipes or input a dish name for step-by-step instructions.</p>', unsafe_allow_html=True)
        if st.button("Get Started"):
            switch_to_chat()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.image("freefood.png", width=400)
    
    st.markdown('<p class="contributors">@Copyright: Joseph Murasa</p>', unsafe_allow_html=True)

def chat_page():
    st.title("Recipe Generator Chat")
    
    # Initialize Groq LLM
    llm = ChatGroq(
        groq_api_key=os.environ['GROQ_API_KEY'],
        model_name="mixtral-8x7b-32768"
    )

    # Setup prompt template
    prompt = ChatPromptTemplate.from_template("""
        You are a smart recipe assistant. Provide answers to recipe-related questions based only on the given context.
        Make sure to offer detailed and step-by-step guidance to help the user.

        <context>
        {context}
        </context>

        Question: {input}

        Your Answer:
    """)

    # Create chains
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Chat interface
    user_input = st.text_input("What would you like to cook today?")

    if user_input:
        with st.spinner('Generating recipe suggestions...'):
            start = time.process_time()
            response = retrieval_chain.invoke({"input": user_input})
            st.write(response['answer'])
            
    # Add a button to return to home
    if st.button("← Back to Home"):
        st.session_state.page = 'home'
        st.rerun()

# Main app logic
def main():
    if st.session_state.page == 'home':
        home_page()
    else:
        chat_page()

if __name__ == "__main__":
    main()