from enum import Enum


class AgentType(str, Enum):

    INTENT = "intent"

    RETRIEVAL = "retrieval"

    RESPONSE = "response"

    SENTIMENT = "sentiment"

    ESCALATION = "escalation"

    CONVERSATION = "conversation"