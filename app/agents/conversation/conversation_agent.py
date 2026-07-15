"""
Purpose:
--------
Maintains conversation context between customer interactions.

Responsibilities:
-----------------
1. Track previous messages.
2. Store session history.
3. Resolve references.
4. Support multi-turn conversations.

Examples:
---------
Customer:
Where is my order?

Customer:
Can I return it?

Conversation Agent:
"It" -> Order
"""

from app.agents.base.base_agent import (
    BaseAgent
)


class ConversationAgent(
    BaseAgent
):

    def execute(
        self,
        state
    ):

        # Future:
        # Retrieve conversation history
        # from Redis or SQL.

        history = state.get(
            "history",
            []
        )

        history.append(
            # state["query"]

            "query":state["query"]

            "intent":state["intent"]

            "response":state["response"]
            
        )

        state["history"] = history

        return state