#!/usr/bin/env python3
"""
Auth Module
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Takes in a password string arguments and returns bytes
    """
    return hashpw(password.encode('utf-8'), gensalt())
