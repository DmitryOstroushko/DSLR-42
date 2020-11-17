"""
Function to define arguments list from command line
"""
import argparse


def options_parse_fa() -> argparse.Namespace:
    """
    Function to define arguments list from command line: filename, print option
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        type=str,
                        help="A name for input dataset")
    parser.add_argument('--print_all', '-a',
                        action="store_true",
                        dest="print_all",
                        help='If set, drawing scatter for all pairs of courses')
    return parser.parse_args()


def options_parse_f() -> argparse.Namespace:
    """
    Function to define arguments list from command line: filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        type=str,
                        help="A name for input dataset")
    return parser.parse_args()
