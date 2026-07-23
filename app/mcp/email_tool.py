from app.mcp.base_tool import (
    BaseTool
)


class EmailTool(
    BaseTool
):

    def execute(
        self,
        email
    ):

        return {

            "email": email,

            "status": "Sent"

        }