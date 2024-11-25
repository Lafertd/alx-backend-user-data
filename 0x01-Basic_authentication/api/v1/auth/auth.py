#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

class Auth:
    """
    Auth class to manage API authentication.

    This class provides a template for handling authentication in an API.
    It defines methods to determine whether authentication is required for
    specific routes, validate the presence of authorization headers, and
    retrieve the current user based on the request.

    Methods:
        - require_auth(path: str, excluded_paths: List[str]) -> bool:
          Determines if a path requires authentication.
        - authorization_header(request=None) -> str:
          Retrieves the Authorization header from a request.
        - current_user(request=None) -> TypeVar('User'):
          Identifies and returns the current user making the request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if the given path requires authentication.

        Args:
            path (str): The URL path being accessed.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if authentication is required for the given path, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the Authorization header if present, otherwise None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user associated with the request.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): The user object associated with the request if available, otherwise None.
        """
        return None

