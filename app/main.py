from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from prompts import SYSTEM_PROMPT
from models import llm
import streamlit as st




#chatbot header
st.header("Seora Assistance")




#define chat history 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SYSTEM_PROMPT]


#print chat history one by one 
for chat in st.session_state.chat_history:
    if isinstance(chat, SystemMessage): continue
    role = "assistant" if isinstance(chat, AIMessage) else "user"

    with st.chat_message(role):
        st.write(chat.content)





#user input 
user_input = st.chat_input("Say something..")


if user_input:
    if user_input.strip().lower() in {'stop','exit','break'}:
        st.stop()

    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message('user'):
        st.write(user_input)
    try:
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.chat_history)
    except Exception as e:
        st.error(str(e))

    st.session_state.chat_history.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)

    
