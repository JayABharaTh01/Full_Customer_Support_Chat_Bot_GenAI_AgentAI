from app.agents.orchestrator.router import (
    AgentRouter
)

router = AgentRouter()

result = router.run(

    {

        "request_id": "1",

        "session_id": "1",

        "user_id": "1",

        "query":
        "I am angry. Where is my refund?",

        "intent": "",

        "intent_confidence": 0.0,

        "sentiment": "",

        "context": "",

        "response": "",

        "escalation": False,

        "history": [],

        "metadata": {},

        "tokens_used": 0,

        "latency": 0

    }

)

print(result)