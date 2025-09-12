import os

from mcp.server.fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

# Create an MCP server
mcp = FastMCP(
    "Demo",
    host="0.0.0.0",
    port=8000,
)


@mcp.custom_route("/health", methods=["GET"])
def health_check(request: Request):
    return JSONResponse(content={"status": "ok"})


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # MCP_SERVER_MODE: stdio | streamable-http | sse
    MCP_SERVER_MODE = os.environ.get("MCP_SERVER_MODE", "streamable-http").lower()
    mcp.run(transport=MCP_SERVER_MODE)
