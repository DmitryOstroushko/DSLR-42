#!/usr/bin/env python3
"""
The module contains functions for LOGREG_TRAIN script: it trains the model (the Class)

  Typical usage example:

  args = options_parse()
"""

import numpy as np  # type: ignore
from csv_utils import load_csv
from data_utils import preprocessing
from logreg import MyLogisticRegressionClass
from stream_funcs import success_message, normal_message
from arg_utils import options_parse_model


def do_main_function():
    """
    Main function of LOG_TRAIN command in the project.
    The function reads data from csv file, selects features and target (name of houses).
    Selected (cleared) data is source for the model
    """
    args = options_parse_model()
    print('Loading data ...')
    dataset = load_csv(args, True)
    print('Preprocessing data ...')
    _, features, data = preprocessing(dataset)
    print('Features are: ', features[1:])
    lrc = MyLogisticRegressionClass()
    print('Model fitting ...')
    thetas = lrc.fit(data, features)
    np.save(args.thetas_file, thetas)
    success_message("Array of coefficients is saved to file " + args.thetas_file + '.npy')
    print('Accuracy scoring ...')
    normal_message("Score = " + str(lrc.score(data, features)))
    print('Done!')


if __name__ == '__main__':
    do_main_function()
