from app.mcp.base_tool import (
    BaseTool
)


class PaymentTool(
    BaseTool
):

    def execute(
        self,
        payment_id
    ):

        return {

            "payment_id": payment_id,

            "status": "Completed"

        }