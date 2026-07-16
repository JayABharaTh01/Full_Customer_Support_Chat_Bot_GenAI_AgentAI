"""
Purpose:
--------
LangGraph Orchestration Layer.

Responsibilities:
-----------------
1. Define agent workflow.
2. Connect agents using edges.
3. Compile the graph.
4. Execute the graph.

Workflow:
---------
Intent
    ↓
Sentiment
    ↓
Conversation
    ↓
Retrieval
    ↓
Response
    ↓
Escalation
"""

# from langgraph.graph import StateGraph
# from langgraph.graph import START, END

# from app.agents.orchestrator.state import AgentState

# from app.agents.intent.intent_agent import IntentAgent
# from app.agents.sentiment.sentiment_agent import SentimentAgent
# from app.agents.conversation.conversation_agent import ConversationAgent
# from app.agents.retrieval.retrieval_agent import RetrievalAgent
# from app.agents.response.response_agent import ResponseAgent
# from app.agents.escalation.escalation_agent import EscalationAgent


# # -----------------------------------
# # Create Graph
# # -----------------------------------

# graph = StateGraph(AgentState)


# # -----------------------------------
# # Add Nodes
# # -----------------------------------

# graph.add_node(
#     "intent",
#     IntentAgent().execute
# )

# graph.add_node(
#     "sentiment",
#     SentimentAgent().execute
# )

# graph.add_node(
#     "conversation",
#     ConversationAgent().execute
# )

# graph.add_node(
#     "retrieval",
#     RetrievalAgent().execute
# )

# graph.add_node(
#     "response",
#     ResponseAgent().execute
# )

# graph.add_node(
#     "escalation",
#     EscalationAgent().execute
# )


# # -----------------------------------
# # Add Edges
# # -----------------------------------

# graph.add_edge(
#     START,
#     "intent"
# )

# graph.add_edge(
#     "intent",
#     "sentiment"
# )

# graph.add_edge(
#     "sentiment",
#     "conversation"
# )

# # graph.add_conditional_edges(
# #     "intent",
# #     route_workflow
# # )

# graph.add_edge(
#     "conversation",
#     "retrieval"
# )

# graph.add_edge(
#     "retrieval",
#     "response"
# )

# graph.add_edge(
#     "response",
#     "escalation"
# )

# graph.add_edge(
#     "escalation",
#     END
# )


# # -----------------------------------
# # Compile Graph
# # -----------------------------------

# compiled_graph = graph.compile()

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.agents.orchestrator.state import (
    AgentState
)

from app.agents.intent.intent_agent import (
    IntentAgent
)

from app.agents.sentiment.sentiment_agent import (
    SentimentAgent
)

from app.agents.conversation.conversation_agent import (
    ConversationAgent
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


graph = StateGraph(
    AgentState
)


graph.add_node(
    "intent",
    IntentAgent().execute
)

graph.add_node(
    "sentiment",
    SentimentAgent().execute
)

graph.add_node(
    "conversation",
    ConversationAgent().execute
)

graph.add_node(
    "retrieval",
    RetrievalAgent().execute
)

graph.add_node(
    "response",
    ResponseAgent().execute
)

graph.add_node(
    "escalation",
    EscalationAgent().execute
)


graph.add_edge(
    START,
    "intent"
)

graph.add_edge(
    "intent",
    "sentiment"
)

graph.add_edge(
    "sentiment",
    "conversation"
)

graph.add_edge(
    "conversation",
    "retrieval"
)

graph.add_edge(
    "retrieval",
    "response"
)

graph.add_edge(
    "response",
    "escalation"
)

graph.add_edge(
    "escalation",
    END
)

compiled_graph = graph.compile()