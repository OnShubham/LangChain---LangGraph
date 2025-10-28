from dotenv import load_dotenv
load_dotenv()
import time
from langchainhub import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import OpenAI
from langchain_tavily import TavilySearch

tools = [TavilySearch()]

def main():
    print("Hello from search-agent!")


if __name__ == "__main__":
    main()
