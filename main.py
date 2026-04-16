from dotenv import load_dotenv
from pydantic import BaseModel
# from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-4-5")
response = llm.invoke("What is the meaning of life?")
print(response)

