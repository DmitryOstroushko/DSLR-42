"""
The module contains functions to create and handle of logger object for the program
"""

import argparse
import logging


def get_file_handler(args: argparse.Namespace) -> logging.FileHandler:
    """
    The function returns FileHandler for logger.
    A file name is defined in log_file_name parameter.
    Level of logging defines is DEBUG.

    Args:
        args: a list of the program parameters as argparse.Namespace object

    Returns:
        FileHandler object for a logger
    """
    file_handler = logging.FileHandler(args.log_file_name)
    file_handler.setLevel(logging.DEBUG)
    return file_handler


def get_stream_handler() -> logging.StreamHandler:
    """
    The function returns StreamHandler for logger.
    Level of logging defines is INFO.

    Returns:
        StreamHandler object for a logger
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    return stream_handler


def get_logger(name: str, args: argparse.Namespace) -> logging.Logger:
    """
    The function returns a logger object with FileHandler object.
    A file name is defined in log_file_name parameter.
    Level of logging defines is DEBUG.

    Args:
        name: a name of a program to print in a log line
        args: a list of the program parameters as argparse.Namespace object

    Returns:
        FileHandler object for a logger
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) "
               "- %(message)s",
        filemode="w",
        filename=args.log_file_name
    )
    logger = logging.getLogger(name)
    logger.addHandler(get_file_handler(args))
    return logger
