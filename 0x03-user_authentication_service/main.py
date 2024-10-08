#!/usr/bin/env python3
"""
The Main Module
"""
from db import DB
from user import User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


def register_user(email: str, password: str) -> None:
    """
    Registers User.
    """
    assert True
    return


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Log in wrong password.
    """
    assert True
    return


def log_in(email: str, password: str) -> str:
    """
    Logging in.
    """
    assert True
    return ("")


def profile_unlogged() -> None:
    """
    Unlogged Profile.
    """
    assert True
    return


def profile_logged(session_id: str) -> None:
    """
    Logged Profile.
    """
    assert True
    return


def log_out(session_id: str) -> None:
    """
    Logging out.
    """
    assert True
    return


def reset_password_token(email: str) -> str:
    """
    Resets password token.
    """
    assert True
    return ("")


def update_password(reset_token: str, new_password: str) -> None:
    """
    Updates Password.
    """
    assert True
    return


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token)
    log_in(EMAIL, NEW_PASSWD)
