"""
Functions to log of application processing
"""

import argparse
import logging


def get_file_handler(args: argparse.Namespace) -> logging.FileHandler:
    """
    To get FileHandler for logger
    """
    file_handler = logging.FileHandler(args.log_file_name)
    file_handler.setLevel(logging.DEBUG)
    return file_handler


def get_stream_handler() -> logging.StreamHandler:
    """
    To get StreamHandler for logger
    """
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    return stream_handler


def get_logger(name: str, args: argparse.Namespace) -> logging.Logger:
    """
    To get Logger object
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
