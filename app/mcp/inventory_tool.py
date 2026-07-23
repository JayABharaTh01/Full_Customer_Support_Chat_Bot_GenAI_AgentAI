from app.mcp.base_tool import (
    BaseTool
)


class InventoryTool(
    BaseTool
):

    def execute(
        self,
        sku
    ):

        return {

            "sku": sku,

            "available": True,

            "quantity": 25

        }