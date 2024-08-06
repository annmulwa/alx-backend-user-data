#!/usr/bin/env python3
"""
Basic authentication module for the API.
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Basic authentication class.
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64
        string base64_authorization_header
        """
        if type(base64_authorization_header) == str:
            try:
                res_decoded = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res_decoded.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
