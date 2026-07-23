"""
Purpose:
--------
Fetch order details.
"""

from app.mcp.base_tool import (
    BaseTool
)


class OrderTool(
    BaseTool
):

    def execute(
        self,
        order_id
    ):

        return {

            "order_id": order_id,

            "status": "Shipped",

            "eta": "Tomorrow"

        }