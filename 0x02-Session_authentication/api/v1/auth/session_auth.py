#!/usr/bin/env python3
""" Module: Session authentication
"""
from api.v1.auth.auth import Auth
import uuid
class SessionAuth(Auth):
    """ Class that serves as the base for session authentication
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that creates a Session ID for a user_id
        Args:
        - user_id (str): the user ID
        Returns:
         - session_id (str): Session ID for the user_id
        """

        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id #retrieve a user_id (v) by session_id (k)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Method that returns the User ID based on the Session ID
         Args:
          - session_id (str): session ID of a User
        Returns:
          - user_id (str): the User Id for a session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        sa = SessionAuth.__dict__.get('user_id_by_session_id')
        for key in sa:
            if key == session_id:
                user_id = sa[key]
                return user_id
