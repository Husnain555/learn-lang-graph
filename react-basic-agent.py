from re import search

from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_tavily import TavilySearch
load_dotenv()
search_tool = TavilySearch(search_depth="basic")
llm = ChatGoogleGenerativeAI(model ="gemini-2.0-flash")
agent  = initialize_agent(tools=[search_tool],llm=llm,agent="structured-chat-zero-shot-react-description",verbose=True)
result = agent.invoke("What was the date of the last SpaceX mission, and how many days ago (or from now) is that?")
print(result)