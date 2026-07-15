"""
Purpose:
--------
OpenAI GPT client.

Models:
-------
gpt-4o
gpt-4o-mini
"""

from openai import OpenAI

from app.config.settings import settings

from app.llm.base_llm import BaseLLM


class OpenAIClient(BaseLLM):

    def __init__(self):

        self.client = OpenAI(

            api_key=settings.OPENAI_API_KEY

        )

        self.model = settings.OPENAI_MODEL

    def generate(
        self,
        prompt
    ):

        response = (

            self.client.chat.completions.create(

                model=self.model,

                messages=[

                    {

                        "role": "user",

                        "content": prompt

                    }

                ],

                temperature=0.2,

                max_tokens=512

            )

        )

        return response.choices[0].message.content

    def stream(
        self,
        prompt
    ):

        pass