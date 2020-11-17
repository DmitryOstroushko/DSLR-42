#!/usr/bin/env python3
"""
Scatter plot function
"""

import sys
from typing import List
from math import sqrt
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from csv_utils import load_csv
from data_utils import preprocessing, get_house_data
from arg_utils import options_parse_fa
from fmath import mean_


def plot_scatter(x_data: List[np.array], y_data: List[np.array], legend: List[str],
                 title: str, xy_labels: List[str]) -> None:
    """
    The function plots scatter for one pair of courses
    """
    colors = [plt.cm.tab10(i/float(len(legend)-1)) for i in range(len(legend))]
    for idx, _ in enumerate(x_data):
        plt.scatter(x_data[idx], y_data[idx], color=colors[idx], alpha=0.5)
    plt.legend(legend, loc='upper right', frameon=False)
    plt.title(title)
    plt.xlabel(xy_labels[0])
    plt.ylabel(xy_labels[1])
    plt.show()


def calc_and_plot(houses: List[str], features: np.array, data_house: List[np.array],
                  idx: int, idx_vs: int) -> None:
    """
    The function calculates and plots scatter plot for one pair of courses
    """
    data_x: List[np.array] = []
    data_y: List[np.array] = []
    for house_idx, _ in enumerate(houses):
        data_single_house = data_house[house_idx]
        data_x.append(np.array(data_single_house[:, idx], dtype=float))
        data_y.append(np.array(data_single_house[:, idx_vs], dtype=float))
    plot_scatter(data_x, data_y, legend=houses,
                 title=features[idx] + "(" + str(idx) + ") vs " +
                 features[idx_vs] + "(" + str(idx_vs) + ")",
                 xy_labels=[features[idx], features[idx_vs]])


def drop_nan(dataset: List[np.array], q_features: int) -> List[np.array]:
    """
    The function drops rows with nan values and returns new data set
    """
    result: List[np.array] = []
    for data in dataset:
        values = np.array(data[1:], dtype=np.float64)
        if len(values[~np.isnan(values)]) + 1 != q_features:
            continue
        result.append(data)
    return np.array(result, dtype=object)


def get_similar_pairs(data: np.array, features: np.array) -> List[int]:
    """
    To define similar pair of features
    """
    similar_features: List[int] = []
    min_similarity = 0.
    for idx, _ in enumerate(features):
        feature_1 = data[:, idx]
        mean_1 = mean_(feature_1)
        for idx_vs in range(idx + 1, len(features)):
            feature_2 = data[:, idx_vs]
            mean_2 = mean_(feature_2)
            similarity = sum((feature_1 - mean_1) * (feature_2 - mean_2)) / \
                sqrt((sum((feature_1 - mean_1)**2) * sum((feature_2 - mean_2)**2)))
            # print(idx, ' - ', idx_vs, ' = ', (similarity))
            if not similar_features or min_similarity > similarity:
                similar_features = [idx + 1, idx_vs + 1]
                min_similarity = similarity
    # print(type(similar_features))
    # print(similar_features)
    return similar_features


def do_main_function():
    """
    Main function of SCATTER_PLOT command in logistic regression project
    """
    args = options_parse_fa()
    dataset = load_csv(args.filename)
    houses, features, data = preprocessing(dataset)
    house_data = get_house_data(data, houses)

    plt.gcf().canvas.set_window_title('Scatter Matrix')

    data_similar = drop_nan(data, len(features))
    similar_features = get_similar_pairs(data_similar[:, 1:], features[1:])

    if args.print_all:
        for idx in range(1, len(features)):
            for idx_vs in range(idx + 1, len(features)):
                plt.gcf().canvas.set_window_title('Scatter Matrix')
                calc_and_plot(houses, features, house_data, idx, idx_vs)

    plt.gcf().canvas.set_window_title('The similar features')
    if similar_features:
        print('The similar features are:')
        print(f'{features[similar_features[0]]} and {features[similar_features[1]]}')
        plt.gcf().canvas.set_window_title('The similar features')
        calc_and_plot(houses, features, house_data, similar_features[0], similar_features[1])
    else:
        feature_1 = input('Input number of 1st feature: ')
        feature_2 = input('Input number of 2nd feature: ')
        try:
            calc_and_plot(houses, features, house_data, int(feature_1), int(feature_2))
        except (ValueError, TypeError):
            print(sys.exc_info()[1])
            print("You should input int values in range 1 - " + str(len(features) - 1))


if __name__ == '__main__':
    do_main_function()
