"""
Exceptions for the project
"""


class NoDataException(Exception):
    """
    NoDataException class throws an exception if data is absent
    """

    def __init__(self, message: str) -> None:
        self.message = message
