"""
The module contains Classes with Exceptions for the project
"""


class NoDataException(Exception):
    """
    NoDataException class throws an exception if data is absent

    Attributes:
        message: a message of the exception
    """

    def __init__(self, message: str) -> None:
        """Initializes NoDataException class with initial values"""
        super().__init__()
        self.message = message
