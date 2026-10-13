from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv()

import asyncio


import sys
from pathlib import Path

MATH_SERVER_PATH = str(Path(__file__).parent / "mathserver.py")

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": sys.executable,
                "args": [MATH_SERVER_PATH],
                "transport": "stdio"
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http"
            }
        }
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="qwen/qwen3.8-27b")
    agent=create_react_agent(model,tools=tools)
    
    math_response = await agent.ainvoke({"messages":[{"role":"user","content":"what is (5+10)*2?"}]})
    print("math response",math_response['messages'][-1].content)
    
    weather_response = await agent.ainvoke({"messages":[{"role":"user","content":"what is the weather in new york?"}]})
    print("weather response",weather_response['messages'][-1].content)

    

if __name__ == "__main__":
    asyncio.run(main())