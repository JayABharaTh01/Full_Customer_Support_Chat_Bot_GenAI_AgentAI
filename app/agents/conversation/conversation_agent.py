"""
Purpose:
--------
Maintains conversation context.

Future:
-------
Redis
PostgreSQL
LangGraph Memory
"""

from app.agents.base.base_agent import (
    BaseAgent
)

from app.memory.memory_manager import (
    MemoryManager
)


class ConversationAgent(
    BaseAgent
):

    def __init__(self):

        self.memory = MemoryManager()

    def execute(
        self,
        state
    ):

        message = {

            "query": state["query"],

            "intent": state.get(
                "intent"
            ),

            "response": state.get(
                "response"
            )

        }

        # Save message in memory
        self.memory.save(

            state["session_id"],

            message

        )

        # Retrieve conversation history
        state["history"] = (

            self.memory.load(

                state["session_id"]

            )

        )

        return state