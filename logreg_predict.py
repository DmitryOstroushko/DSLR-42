#!/usr/bin/env python3
"""
Scrip which predicts the Class for data set
"""

import sys
import argparse
import numpy as np  # type: ignore
from logreg import MyLogisticRegressionClass
from csv_utils import load_csv, save_houses
from data_utils import preprocessing
from stream_funcs import error_message, success_message


def options_parse() -> argparse.Namespace:
    """
    Function to define arguments list for command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset",
                        type=str,
                        help="A name for input dataset")
    parser.add_argument("thetas_file",
                        type=str,
                        help="A name for coefficients of Logistic Regression")
    return parser.parse_args()


def do_main_function():
    """
    The main function of the script
    """
    args = options_parse()
    dataset = load_csv(args.dataset)
    _, features, data = preprocessing(dataset)

    try:
        thetas = np.load(args.thetas_file)
    except FileNotFoundError:
        error_message('It is impossible to find and open file with thetas array')
        error_message(str(sys.exc_info()[1].args[1]))
        sys.exit(-1)

    lrc = MyLogisticRegressionClass(thetas=thetas)
    data_x, _ = lrc.processing(data, features)
    predicts = lrc.predict(data_x)
    save_houses(predicts)
    success_message("Predictions saved to houses.csv")


if __name__ == '__main__':
    do_main_function()
