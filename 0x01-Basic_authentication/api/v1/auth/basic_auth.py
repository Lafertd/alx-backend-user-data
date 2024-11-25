#!/usr/bin/env python3
""" 
Module: basic_auth.py

The BasicAuth class inherits from the Auth class and will be used 
to manage basic authentication features.
"""
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    Currently, it does not implement any specific functionality.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Args:
        authorization_header: header that contains the authentication type and token

        Return:
        the Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None or not isinstance(authorization_header, str) or not authorization_header.startswith("Basic "):
            return None
        else:
            token = authorization_header.split(" ", 1)[1]
            return token

def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
    """
    Decodes a Base64-encoded authorization header.

    Args:
        base64_authorization_header (str): The Base64 string to decode.

    Returns:
        str: The decoded string if valid, otherwise None.
    """
    if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
        return None

    try:
        # Decode the Base64 string
        decoded_bytes = base64.b64decode(base64_authorization_header, validate=True)
        return decoded_bytes.decode('utf-8')  # Convert bytes to string
    except (base64.binascii.Error, UnicodeDecodeError):
        # Handle invalid Base64 or decoding errors
        return None
