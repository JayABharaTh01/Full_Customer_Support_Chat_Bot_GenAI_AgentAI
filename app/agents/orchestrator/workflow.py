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


# class ConversationAgent(
#     BaseAgent
# ):

#     def execute(
#         self,
#         state
#     ):

#         history = state.get(
#             "history",
#             []
#         )

#         history.append(

#             {

#                 "query": state["query"],

#                 "intent": state.get(
#                     "intent"
#                 ),

#                 "response": state.get(
#                     "response"
#                 )

#             }

#         )

#         state["history"] = history

#         return state

"""
Purpose:
--------
Defines business workflows.
"""


class WorkflowManager:

    WORKFLOWS = {

        "refund": [

            "intent",

            "sentiment",

            "conversation",

            "retrieval",

            "response",

            "escalation"

        ],

        "order": [

            "intent",

            "conversation",

            "retrieval",

            "response"

        ],

        "recommendation": [

            "intent",

            "conversation",

            "retrieval",

            "response"

        ]

    }