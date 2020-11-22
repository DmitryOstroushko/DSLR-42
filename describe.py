#!/usr/bin/env python3
"""
The module contains functions for DESCRIBE script: to display an information
about numerical features of dataset

  Typical usage example:

  args = options_parse()
  dict_num_features = set_numerical_features(features, dataset, logger)
  describe_vertical(args, logger)
  describe_horizontal(args, logger)
"""

import argparse
from exceptions import NoDataException
from typing import List
from logging import Logger
import numpy as np  # type: ignore
from stream_funcs import error_message
from csv_utils import load_csv
from fmath import count_, mean_, std_, min_, max_, percentile_25_, percentile_50_, \
    percentile_75_
from app_logger import get_logger


FUNCTION_LIST = {'Count': count_,
                 'Mean': mean_,
                 'Std': std_,
                 'Min': min_,
                 '25%': percentile_25_,
                 '50%': percentile_50_,
                 '75%': percentile_75_,
                 'Max': max_}


def options_parse() -> argparse.Namespace:
    """
    The function extracts arguments of command line and
    returns them as parameters of the program.
    A validation is performing in argparse library module.
    The function processes 4 parameters:
        - 'filename_dataset': name of file with data
        - printing mode
        - whether to get 'index' filed as a feature
        - a log file name: to specify file name for logger, default = 'log.txt'

    Returns:
        Parameters list as argparse.Namespace object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_dataset",
                        type=str,
                        help="A name for input dataset")
    parser.add_argument("--print_mode",
                        "-p",
                        action="store",
                        dest="print_mode",
                        default="v",
                        help="To print horizontally: h, vertically: v")
    parser.add_argument("--index",
                        "-i",
                        action="store_true",
                        dest="index",
                        help="To include index column from features")
    parser.add_argument("--log_file_name",
                        "-f",
                        action="store",
                        dest="log_file_name",
                        default="log.txt",
                        help="Filename for logging of function processing")
    return parser.parse_args()


def set_numerical_features(features: List[str], dataset: np.array, logger: Logger = None) -> dict:
    """
    The function gets a list of name of features, analyses data for each feature
    and marks each feature as numeric or not.

    Args:
        features: a list of name of features
        dataset: a data set as a NUMPY array
        logger: object for logging a scrip

    Returns:
        A dictionary where keys are names of feature, values are boolean marks
        (True if feature is numerical)
    """
    if logger is not None:
        logger.debug("Getting of list of numerical feature")
    numerical_features = dict.fromkeys(features, True)
    for idx, feature in enumerate(features):
        try:
            data = np.array(dataset[:, idx], dtype=float)
            data = data[~np.isnan(data)]
            if not data.any():
                raise NoDataException("No numerical data in column " + feature)
        except (ValueError, TypeError, NoDataException):
            if logger is not None:
                logger.error("No numerical data in column " + feature)
            numerical_features[feature] = False
    if logger is not None:
        logger.info("\nNumerical features are: " + str([key for key, value
                                                        in numerical_features.items() if value]))
    return numerical_features


def describe_vertical(args: argparse.Namespace, logger: Logger) -> None:
    """
    The function gets filename as a parameter, prints results for each feature in rows
    Options: logging of process

    Args:
        args: a list of the program parameters as argparse.Namespace object
        logger: object for logging a script
    """
    logger.info("Printing mode is vertical: printing of metrics in rows")
    dataset = load_csv(args)
    if not args.index:
        dataset = np.delete(dataset, 0, axis=1)
        logger.debug("Column index is deleted")
    features = dataset[0]
    dataset = dataset[1:]
    numerical_features = set_numerical_features(features, dataset, logger)
    print(f'{"":15}', end='')
    logger.debug("Printing of table title: names of numerical features")
    for feature in features:
        if numerical_features[feature]:
            print(f' |{feature:12.12}', end='')
    print()
    logger.debug("OK")

    logger.debug("Printing of table: values of numerical features")
    for function in FUNCTION_LIST:
        print(f'{function:15}', end='')
        logger.debug("Printing of table: function " + function)
        for idx, feature in enumerate(features):
            if numerical_features[feature]:
                data = np.array(dataset[:, idx], dtype=float)
                data = data[~np.isnan(data)]
                print(f' |{FUNCTION_LIST[function](data):>12.4f}', end='')
                logger.debug(feature + ": OK")
        print()
        logger.debug("Printing of table: function " + function + ": OK")
    logger.debug("Printing of table: values of numerical features: OK")


def describe_horizontal(args: argparse.Namespace, logger: Logger) -> None:
    """
    The function gets filename as a parameter, prints results for each feature in columns
    Options: logging of process

    Args:
        args: a list of the program parameters as argparse.Namespace object
        logger: object for logging a script
    """
    logger.info("Printing mode is horizontal: printing of metrics in columns")
    dataset = load_csv(args)
    if not args.index:
        dataset = np.delete(dataset, 0, axis=1)
        logger.debug("Column index is deleted")
    features = dataset[0]
    dataset = dataset[1:]
    logger.debug("Printing of table title: names of functions")
    print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |'
          f'{"50%":>12} |{"75%":>12} |'f'{"Max":>12}')
    logger.debug("OK")

    numerical_features = set_numerical_features(features, dataset, logger)
    logger.debug("Printing of table: values of numerical features")
    for idx, feature in enumerate(features):
        if not numerical_features[feature]:
            continue
        logger.debug("Printing of table: feature " + feature)
        print(f'{feature:15.15}', end=' |')
        data = np.array(dataset[:, idx], dtype=float)
        data = data[~np.isnan(data)]
        for function in FUNCTION_LIST:
            print(f' {FUNCTION_LIST[function](data):>12.4f}|', end='')
        print()
        logger.debug("Printing of table: feature " + feature + ": OK")
    logger.debug("Printing of table: values of numerical features: OK")


def do_main_function() -> None:
    """
    Main function of DESCRIBE script
    """
    args = options_parse()
    logger = get_logger("DESCRIBE application", args)
    logger.info("DESCRIBE function is started ")
    if args.print_mode == 'v':
        describe_vertical(args, logger)
    elif args.print_mode == 'h':
        describe_horizontal(args, logger)
    else:
        logger.error("Wrong print mode: you should use 'h' (horizontal) or "
                     "'v' (vertical) for printing")
        error_message("Wrong print mode: you should use 'h' (horizontal) or "
                      "'v' (vertical) for printing")
    logger.info("DESCRIBE function is finished")


if __name__ == '__main__':
    do_main_function()
