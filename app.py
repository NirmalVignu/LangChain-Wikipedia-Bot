#import streamlit
import streamlit as st

#importing langchain necessary modules
from langchain.llms import OpenAI
from langchain.agents import initialize_agent,load_tools,AgentType

#setting up openai api key
import os
os.environ['OPENAI_API_KEY'] = ''

#setting up streamlit title
st.title("LangChain Wikipedia Bot")

#setting up langchain agent
llm=OpenAI(temperature=0)
tools=load_tools(['wikipedia'],llm=llm)
agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)


# streamlit text input and output to display
input=st.text_input("Type your prompt here")
if input:
    text=agent.run(input)
    st.write(text)