from enum import Enum


class IntentType(str, Enum):

    ORDER = "order_tracking"

    REFUND = "refund"

    BILLING = "billing"

    ACCOUNT = "account"

    FAQ = "faq"

    RECOMMENDATION = "recommendation"

    UNKNOWN = "unknown"