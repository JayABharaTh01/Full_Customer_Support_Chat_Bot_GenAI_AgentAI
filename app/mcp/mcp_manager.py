from app.mcp.order_tool import (
    OrderTool
)

from app.mcp.payment_tool import (
    PaymentTool
)

from app.mcp.inventory_tool import (
    InventoryTool
)

from app.mcp.email_tool import (
    EmailTool
)


class MCPManager:

    def __init__(self):

        self.tools = {

            "order": OrderTool(),

            "payment": PaymentTool(),

            "inventory": InventoryTool(),

            "email": EmailTool()

        }

    def execute(
        self,
        tool_name,
        **kwargs
    ):

        tool = self.tools.get(
            tool_name
        )

        if not tool:

            raise ValueError(
                "Tool not found."
            )

        return tool.execute(
            **kwargs
        )