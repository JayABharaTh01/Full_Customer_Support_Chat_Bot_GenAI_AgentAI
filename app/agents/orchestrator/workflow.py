"""
Purpose:
--------
Defines business workflows.

Examples:
---------
- Refund Workflow
- Order Tracking Workflow
- Billing Workflow
- Recommendation Workflow
"""


class WorkflowManager:

    WORKFLOWS = {

        "refund": [

            "intent",

            "retrieval",

            "response",

            "escalation"

        ],

        "order": [

            "intent",

            "retrieval",

            "response"

        ]

    }