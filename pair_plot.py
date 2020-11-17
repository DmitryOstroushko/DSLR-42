#!/usr/bin/env python3
"""
.py script, which displays a pair plot matrix
"""

from typing import List
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
from csv_utils import load_csv
from data_utils import preprocessing, get_house_data, get_one_pair_house_data
from arg_utils import options_parse_f


def pair_plot_scatter(axes, data_x: List[np.array], data_y: List[np.array]) -> None:
    """
    To plot scatter for one pair of courses
    """
    colors = ['red', 'yellow', 'blue', 'green']
    for idx, _ in enumerate(data_x):
        axes.scatter(data_x[idx], data_y[idx], s=1, color=colors[idx], alpha=0.5)


def pair_plot_hist(axes, data: List[np.array]) -> None:
    """
    To plot histogram for single course
    """
    colors = ['red', 'yellow', 'blue', 'green']
    for idx, data_line in enumerate(data):
        axes.hist(data_line[~np.isnan(data_line)], color=colors[idx], alpha=0.5)


def pair_plot(houses: List[str], features: np.array, data_house: List[np.array]) -> None:
    """
    To plot pair matrix
    """
    font = {'family': 'DejaVu Sans',
            'weight': 'light',
            'size': 7}
    plt.rc('font', **font)

    size = len(features) - 1
    _, axes = plt.subplots(nrows=size, ncols=size)
    plt.subplots_adjust(wspace=0.15, hspace=0.15)
    plt.gcf().canvas.set_window_title('Pair Plot')
    for row in range(size):
        for col in range(size):
            data_x, data_y = get_one_pair_house_data(data_house, houses, row + 1, col + 1)

            if col == row:
                pair_plot_hist(axes[row, col], data_x)
            else:
                pair_plot_scatter(axes[row, col], data_x, data_y)

            if axes[row, col].is_last_row():
                axes[row, col].set_xlabel(features[col + 1].replace(' ', '\n'))
            else:
                axes[row, col].tick_params(labelbottom=False)

            if axes[row, col].is_first_col():
                axes[row, col].set_ylabel(features[row + 1].replace(' ', '\n'))
            else:
                axes[row, col].tick_params(labelleft=False)

            axes[row, col].spines['right'].set_visible(False)
            axes[row, col].spines['top'].set_visible(False)

    plt.legend(houses, loc='upper left', frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()


def do_main_function() -> None:
    """
    Main function of PAIR_PLOT command in DSLR project
    """
    args = options_parse_f()
    dataset = load_csv(args.filename)
    houses, features, data = preprocessing(dataset)
    data_house = get_house_data(data, houses)

    pair_plot(houses, features, data_house)


if __name__ == '__main__':
    do_main_function()
