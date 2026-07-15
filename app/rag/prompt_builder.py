"""
Purpose:
--------
Builds prompts for the LLM.
"""


class PromptBuilder:

    SYSTEM_PROMPT = """
You are an AI Customer Support Assistant.

Only answer using the provided context.

If the answer is unavailable,
say:

'I could not find that information.'
"""

    def build(

        self,

        context,

        query

    ):

        return f"""

{self.SYSTEM_PROMPT}

Context:

{context}

Customer Question:

{query}

Answer:
"""