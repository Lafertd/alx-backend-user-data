#!/usr/bin/env python3
""" Module: Session authentication
"""
from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    """ Class that serves as the base for session authentication
    """
    
    def __init__(self, user_id_by_session_id):
        """ Attributes of the Class
        """
	self.user_id_by_session_id = {}

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
		user_id_by_session_id[session_id] = user_id
		return session_id #retrieve a user_id (v) by session_id (k)
