"""
The module contains functions to work with csv files:
- to load data from the dataset as a csv file
- to save a array of predictions to file houses.csv
- to load a list of numbers of features, divided by comma

  Typical usage examples:

  dataset = load_scv(args)
  save_houses(list_of_str)
  features_list = get_features_list(features_list_filename)
"""

import sys
import csv
import argparse
from typing import List, Optional
import numpy as np  # type: ignore
from stream_funcs import error_message, success_message, normal_message


def get_feature_list(features_list_filename: Optional[str]) -> List[int]:
    """
    The function gets a file name with with a list of numbers of features, divided by comma,
    checks a format of data and returns list of numbers of features

    Args:
        features_list_filename: a name for filename with a list of numbers of features,
          divided by comma

    Returns:
        A list of numbers of features as a list of digits
    """
    if features_list_filename is None:
        normal_message('A file with numbers of features is not defined.\n'
                       'A prediction for houses will be performed '
                       'on base entire array of features')
        return []
    try:
        with open(features_list_filename) as csv_file:
            features_list: List[int] = []
            reader = csv.reader(csv_file)
            if not reader:
                normal_message('A file with numbers of features is empty.\n'
                               'A prediction for houses will be performed '
                               'on base entire array of features')
            try:
                for value in list(reader)[0]:
                    features_list.append(int(value))
            except (ValueError, TypeError):
                normal_message('There are incorrect numbers of features in '
                               'the file with numbers of features.\n'
                               'A prediction for houses will be performed '
                               'on base entire array of features')
                return []
            return features_list
    except (FileExistsError, FileNotFoundError, csv.Error):
        data = sys.exc_info()[1]
        if data is not None:
            error_message(f'file {features_list_filename}: {data.args[1]}')
        normal_message('A prediction for houses will be performed on base entire array of features')
        return []


def load_csv(args: argparse.Namespace, if_feature_list: bool = False) -> np.array:
    """
    The function loads data from csv file and returns dataset as a NUMPY array.
    A result array includes only features which numbers are saved in file with name
    defined in features_list_filename. Numbers of features in the file have to be divided by comma
    and should be typed in single row: the function loads from a file only first line.
    If parameter 'features_list_filename' is absent then a result array includes entire data set.

    Args:
        args: parameters list as argparse.Namespace object
        if_feature_list: option ti load feature list from file, uses only
        to train model and predict

    Returns:
        An array of data as a NUMPY array
    """
    try:
        dataset = []
        feature_list = get_feature_list(args.features_list_filename) \
            if if_feature_list else []
        with open(args.filename_dataset) as csv_file:
            reader = csv.reader(csv_file)
            for value_list in reader:
                row = []
                for idx, value in enumerate(value_list):
                    if feature_list and idx > 5 and idx - 5 not in feature_list:
                        continue
                    try:
                        row.append(float(value))
                    except ValueError:
                        except_value = np.nan if not value else value
                        row.append(except_value)
                dataset.append(row)
        return np.array(dataset, dtype=object)
    except (FileExistsError, FileNotFoundError, csv.Error):
        data = sys.exc_info()[1]
        if data is not None:
            error_message(f'file {args.dataset_filename}: {data.args[1]}')
        sys.exit(1)


def save_houses(predictions: List[str]) -> None:
    """
    The function saves an array of predictions to csv file

    Args:
        predictions: a list of strings is predictions of the model
    """
    try:
        with open('houses.csv', 'w') as data_file:
            data_file.write('Index,Hogwarts House\n')
            for key in enumerate(predictions):
                data_file.write('{},{}\n'.format(key[0], key[1]))
        success_message('Thetas array is saved')
    except IOError:
        data = sys.exc_info()[1]
        if data is not None:
            error_message(str(data.args[1]))
        error_message('It is impossible to save predictions')
