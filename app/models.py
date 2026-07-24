from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()



#calling the model 
llm = ChatGroq(model='llama-3.1-8b-instant')