from dotenv import load_dotenv

import time
from langchainhub import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
load_dotenv()
tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_promot = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_promot,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

def main():
    result = chain.invoke(
        input={
            "input": "search for 3 job posting for an ai enginner using langchain in the bay area on linkdin and list their details"
        }
    )
    
    print(result)


if __name__ == "__main__":
    main()
