#!/usr/bin/env python3
# api/v1/auth/auth.py
from flask import request
from typing import List

class Auth:
    """Auth class to manage API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.
        Currently returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header.
        Currently returns None.
        """
        return None

    def current_user(self, request=None) -> 'User':
        """
        Returns the current user.
        Currently returns None.
        """
        return None

