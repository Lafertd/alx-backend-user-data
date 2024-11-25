#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

class Auth:
    """
    Class: Class to manage the API authentication

    Return: work as a 
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Auth: Class to manage the API authentication
        """
        return False
    def authorization_header(self, request=None) -> str:
        """
        Auth: Class to manage the API authentication
        """
        return None
    def current_user(self, request=None) -> TypeVar('User'):
        """
        Auth: Class to manage the API authentication
        """
        return None
