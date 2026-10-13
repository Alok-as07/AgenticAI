from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int,b:int):
    """Add two numbers"""
    return a + b

@mcp.tool()
def sub(a:int,b:int):
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def mul(a:int,b:int):
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def div(a:int,b:int):
    """Divide two numbers"""
    return a / b

@mcp.tool()
def power(base:int,exp:int):
    """Raise base to the power of exp"""
    return base ** exp

if __name__ == "__main__":
    mcp.run(transport="stdio")
    