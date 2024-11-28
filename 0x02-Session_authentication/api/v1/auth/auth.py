#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
import re
import os


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Currently returns False.
        """
        if path is None or excluded_paths in (None, []):
            return True
        # Normalize the input path and excluded paths
        path = path.rstrip('/')
        normalized_excluded_paths = [ep.rstrip('/') for ep in excluded_paths]
        for ep in normalized_excluded_paths:
            regex_pattern = ep.replace('*', '.*')
            if re.match(regex_pattern + '$', path):  # Ensures full path match
                return False
            return True
    
    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header.
        Currently returns None.
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.
        Currently returns None.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a Cookie value.
        """
        _my_session_id = os.getenv("SESSION_NAME", "_my_session_id")
        if request is None:
            return None
        return request.cookies.get(_my_session_id)

