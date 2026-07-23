"""
Purpose:
--------
Expose MCP tools.
"""

from fastapi import APIRouter

from app.mcp.mcp_manager import (
    MCPManager
)

router = APIRouter()

mcp = MCPManager()


@router.post(
    "/mcp/order"
)
def order_tool():

    return mcp.execute(

        "order",

        order_id="123"

    )


@router.post(
    "/mcp/payment"
)
def payment_tool():

    return mcp.execute(

        "payment",

        payment_id="PAY123"

    )


@router.post(
    "/mcp/inventory"
)
def inventory_tool():

    return mcp.execute(

        "inventory",

        sku="SKU123"

    )