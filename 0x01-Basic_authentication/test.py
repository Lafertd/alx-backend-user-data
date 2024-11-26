#!/usr/bin/env python3
""" TEST 
    File: basic_auth.py
"""

from api.v1.auth.basic_auth import BasicAuth
from models.user import User 
import uuid

a = BasicAuth()

             # ________TEST_1_________
""" TEST
    Method: extract_base64_authorization_header(self, authorization_header: str) -> str:
"""
print(a.extract_base64_authorization_header(None))
print(a.extract_base64_authorization_header(89))
print(a.extract_base64_authorization_header("Holberton School"))
print(a.extract_base64_authorization_header("Basic Holberton"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(a.extract_base64_authorization_header("Basic1234"))


             # ________TEST_2_________

""" TEST
    Method: decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
"""
print(a.decode_base64_authorization_header(None))
print(a.decode_base64_authorization_header(89))
print(a.decode_base64_authorization_header("Holberton School"))
print(a.decode_base64_authorization_header("SG9sYmVydG9u"))
print(a.decode_base64_authorization_header("SG9sYmVydG9uIFNjaG9vbA=="))
print(a.decode_base64_authorization_header(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))



            # ________TEST_3_________

""" TEST
    Method: extract_user_credentials(self, decode_base64_authorization_header: str) (str, str):
"""
print(a.extract_user_credentials(None))
print(a.extract_user_credentials(89))
print(a.extract_user_credentials("Holberton School"))
print(a.extract_user_credentials("Holberton:School"))
print(a.extract_user_credentials("bob@gmail.com:toto1234"))



             # ________TEST_4_________

""" TEST
     Method: user_object_from_credentials(self, user_email:str, user_pwd:str) -> TypeVar(User):
"""

print('TEST' + '4')

""" **Create a user test**

user_email = str(uuid.uuid4())
user_clear_pwd = str(uuid.uuid4())
user = User()
user.email = user_email
user.first_name = "Bob"
user.last_name = "Dylan"
user.password = user_clear_pwd
print("New user: {}".format(user.display_name()))
user.save()
"""

""" Retreive this user via the class BasicAuth """

a = BasicAuth()
from file_storage import *

u = a.user_object_from_credentials(None, None)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(89, 98)
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials("email@notfound.com", "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, "pwd")
print(u.display_name() if u is not None else "None")

u = a.user_object_from_credentials(user_email, user_clear_pwd)
print(u.display_name() if u is not None else "None")


            # ________TEST_5__________
