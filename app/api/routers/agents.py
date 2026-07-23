"""
Purpose:
--------
Expose available agents.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/agents")
def get_agents():

    return {

        "agents": [

            {

                "name": "Intent Agent",

                "purpose":
                "Query Classification"

            },

            {

                "name": "Sentiment Agent",

                "purpose":
                "Emotion Detection"

            },

            {

                "name":
                "Conversation Agent",

                "purpose":
                "Conversation Context"

            },

            {

                "name":
                "Retrieval Agent",

                "purpose":
                "RAG Retrieval"

            },

            {

                "name":
                "Response Agent",

                "purpose":
                "Generate Responses"

            },

            {

                "name":
                "Escalation Agent",

                "purpose":
                "Human Escalation"

            }

        ]

    }