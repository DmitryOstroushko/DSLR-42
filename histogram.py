#!/usr/bin/env python3
"""
Histogram function: script displays a histogram
"""

from typing import List
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from data_utils import preprocessing, get_house_data
from csv_utils import load_csv
from arg_utils import options_parse_fa


def plot_histogram(data: List[np.array], legend: List[str], title: str,
                   x_label: str, y_label: str) -> None:
    """
    the function plots histogram for one course
    """
    colors = ['green', 'yellow', 'red', 'blue']
    for idx, data_line in enumerate(data):
        plt.hist(data_line[~np.isnan(data_line)], color=colors[idx], alpha=0.5)
    plt.legend(legend, loc='upper left', frameon=False)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def calc_and_plot(houses: List[str], features: List[str], house_data: List[np.array],
                  idx: int) -> None:
    """
    The function creates array of values for one course.
    After that it invokes the function to plot histogram for one course.
    """
    data_col = []
    for idx_house, _ in enumerate(houses):
        data_col.append(np.array(house_data[idx_house][:, idx], dtype=float))
    plot_histogram(data_col, legend=houses, title=features[idx], x_label='Marks',
                   y_label='A number of students')


def do_main_function() -> None:
    """
    Main function of HISTOGRAM command in DSLR project
    The function calculates score distribution for each course and
    defines the course with the most homogeneous score
    """
    args = options_parse_fa()
    dataset = load_csv(args.filename)
    houses, features, data = preprocessing(dataset)
    house_data = get_house_data(data, houses)

    min_mark_range = np.inf
    idx_homogeneous_feature = 0

    for idx in range(1, len(features)):
        mark_line = np.array(data[:, idx], dtype=float)
        if (max(mark_line) - min(mark_line)) < min_mark_range:
            min_mark_range = max(mark_line) - min(mark_line)
            idx_homogeneous_feature = idx
        if args.print_all:
            plt.gcf().canvas.set_window_title('Score distribution')
            calc_and_plot(houses, features, house_data, idx)

    print(f'The most homogeneous score: course = {features[idx_homogeneous_feature]}, '
          f'marks range = {min_mark_range:.2f}')
    plt.gcf().canvas.set_window_title('The most homogeneous score')
    calc_and_plot(houses, features, house_data, idx_homogeneous_feature)


if __name__ == '__main__':
    do_main_function()
