#!/usr/bin/env python3
""" 
Module: basic_auth.py

The BasicAuth class inherits from the Auth class and will be used 
to manage basic authentication features.
"""
import base64
import binascii
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

        base64_authorization_header = authorization_header.split(" ", 1)[1]
        return base64_authorization_header

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
            decoded_base64 = base64.b64decode(base64_authorization_header, validate=False)
            return decoded_base64.decode("utf-8")
        except binascii.Error:
            return None
    def extract_user_credentials(self, decode_base64_authorization_header: str) -> (str, str):
        """
        Extract user credentials('email : password') from the a Base64-decoded authorization header

        Args:
        decoded_base64_authorization_header (str): the header to extract credentials from.

        Returns:
        tuple(str, str): the extracted credentials seperated by a colon :
        """
        not_string = not isinstance(decode_base64_authorization_header, str)
        if decode_base64_authorization_header is None or not_string or ':' not in decode_base64_authorization_header:
            return None, None
        credentials = tuple(decode_base64_authorization_header.split(':', 2))
        return credentials
