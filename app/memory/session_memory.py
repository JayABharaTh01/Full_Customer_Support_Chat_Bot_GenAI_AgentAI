"""
Purpose:
--------
Maintains active user sessions.
"""


class SessionMemory:

    def __init__(self):

        self.sessions = {}

    def create(
        self,
        session_id
    ):

        self.sessions[
            session_id
        ] = {}

    def exists(
        self,
        session_id
    ):

        return session_id in self.sessions