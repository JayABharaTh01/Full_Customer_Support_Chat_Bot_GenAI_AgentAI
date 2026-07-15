"""
Purpose:
--------
Executes agents sequentially.
"""

from app.agents.intent.intent_agent import (
    IntentAgent
)

from app.agents.sentiment.sentiment_agent import (
    SentimentAgent
)

from app.agents.retrieval.retrieval_agent import (
    RetrievalAgent
)

from app.agents.response.response_agent import (
    ResponseAgent
)

from app.agents.escalation.escalation_agent import (
    EscalationAgent
)

from app.agents.conversation.conversation_agent import (
    ConversationAgent
)

class AgentRouter:

    def __init__(self):

        self.agents = [
            IntentAgent(),

            SentimentAgent(),
            
            ConversationAgent(),
            
            RetrievalAgent(),
            
            ResponseAgent(),
            
            EscalationAgent()
            
            ]

    def run(
        self,
        state
    ):

        for agent in self.agents:

            state = agent.execute(
                state
            )

        return state