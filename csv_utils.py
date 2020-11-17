"""
Functions for data loading and data processing
"""
import sys
import csv
from typing import List
import numpy as np  # type: ignore
from stream_funcs import error_message, success_message


def load_csv(filename: str) -> np.array:
    """
    The function loads data from csv file and returns dataset
    """
    dataset = []
    try:
        with open(filename) as csv_file:
            reader = csv.reader(csv_file)
            for value_list in reader:
                row = []
                for value in value_list:
                    try:
                        row.append(float(value))
                    except ValueError:
                        except_value = np.nan if not value else value
                        row.append(except_value)
                dataset.append(row)
    except (FileExistsError, FileNotFoundError, csv.Error):
        error_message(f'file {filename}: {sys.exc_info()[1]}')
        sys.exit(1)
    return np.array(dataset, dtype=object)


def save_houses(predictions: List[str]) -> None:
    """
    To save array of predictions to csv file
    """
    try:
        with open('houses.csv', 'w') as data_file:
            for key in enumerate(predictions):
                data_file.write('{},{}\n'.format(key[0], key[1]))
        success_message('Thetas array is saved')
    except IOError:
        error_message(str(sys.exc_info()[1].args[1]))
        error_message('It is impossible to save predictions')


def save_thetas(thetas: List[np.array], file_name: str) -> None:
    """
    To save array of thetas coefficients to csv file
    """
    try:
        with open(file_name, 'w') as data_file:
            for key in thetas:
                data_file.write('{}\n'.format(key))
        success_message('Thetas array is saved')
    except IOError:
        error_message(str(sys.exc_info()[1].args[1]))
        error_message('It is impossible to save theta values')
