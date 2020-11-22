#!/usr/bin/env python3
"""
The module contains functions for LOGREG_PREDICT script: it makes predictions for the data set

  Typical usage example:

  args = options_parse()
"""

import sys
import numpy as np  # type: ignore
from logreg import MyLogisticRegressionClass
from csv_utils import load_csv, save_houses
from data_utils import preprocessing
from stream_funcs import error_message, success_message
from arg_utils import options_parse_model


def do_main_function():
    """
    The main function of the script
    """
    args = options_parse_model(True)
    dataset = load_csv(args, True)
    _, features, data = preprocessing(dataset)

    try:
        thetas = np.load(args.thetas_file)
    except FileNotFoundError:
        error_message('It is impossible to find and open file with thetas array')
        error_message(str(sys.exc_info()[1].args[1]))
        sys.exit(-1)

    lrc = MyLogisticRegressionClass(thetas=thetas)
    data_x, _ = lrc.processing(data, features, False)
    try:
        predicts = lrc.predict(data_x)
        save_houses(predicts)
        success_message("Predictions saved to houses.csv")
    except ValueError:
        error_message('Dimensions of the data set, the thetas array are different')
        error_message('It is impossible to predict values for the data set')


if __name__ == '__main__':
    do_main_function()
