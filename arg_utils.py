"""
The module contains standard functions to parse arguments of a command line of a program
and to return parameters list as argparse.Namespace object

There are 3 functions:
    - a function with 2 args: filename for data set and print option
    - a function with 1 arg: filename for data set
    - a function for training model and prediction: vary a number of parameters

  Typical usage example:

  args_1 = options_parse_f()
  args_2 = options_parse_fa()
"""

import argparse


def options_parse_model(is_predict: bool = False):
    """
    The function extracts arguments of command line and
    return them as parameters of the program.
    A validation is performing in argparse library module.

    Returns:
        Parameters list as argparse.Namespace object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_dataset",
                        type=str,
                        help="A name for input dataset")
    parser.add_argument("thetas_file",
                        type=str,
                        help="A name for file for saving of LG coefficients")
    parser.add_argument("-f",
                        dest="features_list_filename",
                        type=str,
                        action="store",
                        help="A name for file with list of numbers of features")
    if is_predict:
        parser.add_argument('-a', '--alpha',
                            dest="alpha",
                            type=int,
                            action="store",
                            help="alpha parameter")
        parser.add_argument('-n', '--n_iter',
                            dest="n_iter",
                            type=int,
                            action="store",
                            help="A number of iterations")
    return parser.parse_args()


def options_parse_f() -> argparse.Namespace:
    """
    The function extracts arguments of command line and
    return them as parameters of the program.
    A validation is performing in argparse library module.
    The function processes 'dataset' parameter: name of file with data

    Returns:
        Parameters list as argparse.Namespace object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_dataset",
                        type=str,
                        help="A name for input dataset")
    return parser.parse_args()


def options_parse_fa() -> argparse.Namespace:
    """
    The function extracts arguments of command line and
    return them as parameters of the program.
    A validation is performing in argparse library module.
    The function processes 2 parameters:
        - 'dataset': name of file with data
        - printing mode

    Returns:
        Parameters list as argparse.Namespace object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename_dataset",
                        type=str,
                        help="A file name for input dataset")
    parser.add_argument('--print_all', '-a',
                        action="store_true",
                        dest="print_all",
                        help='If set, drawing graphs for all pairs of courses')
    return parser.parse_args()
