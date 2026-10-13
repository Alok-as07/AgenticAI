from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location:str):
    """Get weather for location"""
    return f"Weather in {location} is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")