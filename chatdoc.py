import os
from apikey import apikey

import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

os.environ["OPENAI_API_KEY"] = apikey

def clear_history():
    if 'history' in st.session_state:
        del st.session_state['history']

st.title('Chat with Document')
upload_file = st.file_uploader('Upload a file',type=['pdf'])
add_file = st.button('Upload File', on_click=clear_history)
if upload_file and add_file:
    with st.spinner('Reading, chunking and embedding file...'):
        bytes_data = upload_file.read()
        file_name = os.path.join('./', upload_file.name)
        with open(file_name, 'wb') as f:
            f.write(bytes_data)
        
        loader = PyPDFLoader(file_name)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

        chunks = text_splitter.split_documents(documents)

        embeddings = OpenAIEmbeddings()

        vector_store = Chroma.from_documents(chunks, embeddings)

        llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.9)

        retriever = vector_store.as_retriever()
        crc = ConversationalRetrievalChain.from_llm(llm, retriever)
        st.session_state.crc = crc
        st.success('File uploaded, chunked and embedded successfully')

question = st.text_input('Input your question')

if question:
    if 'crc' in st.session_state:
        crc = st.session_state.crc
        if 'history' not in st.session_state:
            st.session_state['history'] = []

        response = crc.run({'question': question, 'chat_history':st.session_state['history']})

        st.session_state['history'].append((question, response))
        st.write(response)

        for prompts in st.session_state['history']:
            st.write("Question: "+prompts[0])
            st.write("Answer: "+prompts[1])

