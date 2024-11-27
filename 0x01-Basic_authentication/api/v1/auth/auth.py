#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


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
        excluded_paths = [ep.rstrip('/', '*$') for ep in excluded_paths]
        # Check if normalized path is in excluded_paths
        if path in excluded_paths:
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
