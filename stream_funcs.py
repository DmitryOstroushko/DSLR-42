"""
Functions for messaging printing
"""


def error_message(message):
    """
    Verbosity for error messaging in red color
    """
    print("\033[31m{:s}\033[0m".format(message))


def success_message(message):
    """
    Verbosity for success messaging in green color
    """
    print("\033[32m{:s}\033[0m".format(message))


def normal_message(message):
    """
    Verbosity for normal messaging as usual
    """
    print(message)
