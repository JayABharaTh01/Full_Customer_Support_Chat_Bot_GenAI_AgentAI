from app.mcp.mcp_manager import (
    MCPManager
)

manager = MCPManager()

result = manager.execute(

    "order",

    order_id="123"

)

print(result)