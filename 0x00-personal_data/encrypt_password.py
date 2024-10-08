#!/usr/bin/env python3
"""
A module for encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
