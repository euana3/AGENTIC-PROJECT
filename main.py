from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent  # Updated for LangGraph V1.0
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

tools = [search_tool, wiki_tool, save_tool]
agent = create_agent(llm, tools)

query = input("What can I help you research? ")
raw_response = agent.invoke({"messages": [HumanMessage(content=query)]})

final_content = raw_response["messages"][-1].content
print("RESEARCH SUMMARY:")
print("=" * 50)
print(final_content)
print("\nSAVED TO: research_output.txt")
save_tool(final_content)