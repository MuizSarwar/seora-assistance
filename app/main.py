from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


#calling the model 
llm = ChatGroq(model='llama-3.1-8b-instant')

#chatbot header
st.header("Seora Assistance")


#define  system message 
system_message = SystemMessage(content="You are a helpful assistance,your task is to give ans with in 1 to 2 sentences.")


#define chat history 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [system_message]


#print chat history one by one 
for chat in st.session_state.chat_history:
    if isinstance(chat, SystemMessage): continue
    role = "assistant" if isinstance(chat, AIMessage) else "user"

    with st.chat_message(role):
        st.write(chat.content)





#user input 
user_input = st.chat_input("Say something..")


if user_input:
    if user_input.strip().lower() == {'stop','exit','break'}:
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message('user'):
        st.write(user_input)

    responce = llm.invoke(st.session_state.chat_history)

    st.session_state.chat_history.append(AIMessage(content=responce.content))
    with st.chat_message("assistant"):
        st.write(responce.content)

    
