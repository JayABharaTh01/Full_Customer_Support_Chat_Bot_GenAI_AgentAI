"""
Purpose:
--------
Frontend UI for Customer Support AI.
"""

import streamlit as st
import requests


API_URL = "http://localhost:8000/api/v1"


st.set_page_config(

    page_title="Customer Support AI",

    page_icon="🤖",

    layout="wide"

)


st.title(
    "🤖 Customer Support AI"
)


session_id = st.sidebar.text_input(

    "Session ID",

    value="session_1"

)


query = st.text_input(

    "Ask a question"
)


if st.button(
    "Submit"
):

    payload = {

        "query": query

    }

    response = requests.post(

        f"{API_URL}/chat",

        params=payload

    )

    st.write(
        "Status Code:",
        response.status_code
    )

    result = response.json()

    # Debug
    st.write(
        "Raw Response:"
    )

    st.json(
        result
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Response"
        )

        st.success(

            result.get(
                "response",
                "N/A"
            )

        )

        st.subheader(
            "Intent"
        )

        st.info(

            result.get(
                "intent",
                "N/A"
            )

        )

        st.subheader(
            "Sentiment"
        )

        st.info(

            result.get(
                "sentiment",
                "N/A"
            )

        )

    with col2:

        st.subheader(
            "Escalation"
        )

        st.warning(

            str(

                result.get(
                    "escalation",
                    False
                )

            )

        )

        st.subheader(
            "Tokens Used"
        )

        st.info(

            result.get(
                "tokens_used",
                0
            )

        )

        st.subheader(
            "Latency"
        )

        st.info(

            str(

                result.get(
                    "latency",
                    0
                )

            )

        )

    st.divider()

    st.subheader(
        "Conversation History"
    )

    history = result.get(
        "history",
        []
    )

    if history:

        for item in history:

            st.write(
                item
            )

    st.divider()

    st.subheader(
        "Agent Execution"
    )

    st.markdown(
        """
- Intent Agent
- Sentiment Agent
- Conversation Agent
- Retrieval Agent
- Response Agent
- Escalation Agent
"""
    )