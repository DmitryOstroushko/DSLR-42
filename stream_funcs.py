"""
The module contains functions for printing of messages in different colours
depending on how operations were successful

  Typical usage example:

  error_message(message)
  success_message(message)
  normal_message(message)
"""


def error_message(message: str) -> None:
    """
    Verbosity for error messaging in red color

    Args:
        message: a text to print
    """
    print("\033[31m{:s}\033[0m".format(message))


def success_message(message: str) -> None:
    """
    Verbosity for success messaging in green color

    Args:
        message: a text to print
    """
    print("\033[32m{:s}\033[0m".format(message))


def normal_message(message: str) -> None:
    """
    Verbosity for normal messaging as usual

    Args:
        message: a text to print
    """
    print(message)
