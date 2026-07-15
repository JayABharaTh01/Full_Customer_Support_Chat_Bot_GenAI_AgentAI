"""
Purpose:
--------
Validates generated responses.
"""


class ResponseValidator:

    def validate(
        self,
        response
    ):

        if len(response) == 0:

            return False

        return True