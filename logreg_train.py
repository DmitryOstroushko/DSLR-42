#!/usr/bin/env python3
"""
Scrip which trains the model (the Class)
"""

import argparse
import numpy as np  # type: ignore
from csv_utils import load_csv
from data_utils import preprocessing
from logreg import MyLogisticRegressionClass
from stream_funcs import success_message, normal_message


def options_parse():
    """
    Function to define arguments list for command line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
                        type=str,
                        help="A name for input dataset")
    parser.add_argument("thetas_file",
                        type=str,
                        help="A name for file for saving of LG coefficients")
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


def do_main_function():
    """
    Main function of LOG_TRAIN command in the project.
    The function reads data from csv file, selects features and target (name of houses).
    Selected (cleared) data is source for the model
    """
    args = options_parse()
    dataset = load_csv(args.filename)
    _, features, data = preprocessing(dataset)
    lrc = MyLogisticRegressionClass()
    thetas = lrc.fit(data, features)
    np.save(args.thetas_file, thetas)
    success_message("Array of coefficients is saved to file " + args.thetas_file)
    normal_message("Score = " + str(lrc.score(data, features)))


if __name__ == '__main__':
    do_main_function()
