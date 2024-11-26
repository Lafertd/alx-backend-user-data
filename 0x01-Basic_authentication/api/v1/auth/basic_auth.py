#!/usr/bin/env python3
""" 
Module: basic_auth.py

The BasicAuth class inherits from the Auth class and will be used 
to manage basic authentication features.
"""
import base64
import binascii
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User

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

    def user_object_from_credentials(self, user_email:str, user_pwd:str) -> TypeVar('User'):
        """ Extract User object based on the user's credentials

        Args:
        user_email (str): email of the user
        user_pwd (str): password of the user

        Returns:
        the instance of the user if the credentials match the user's email and password inside the database
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None
