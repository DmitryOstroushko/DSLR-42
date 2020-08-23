#!/usr/bin/env python3

import argparse
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from stream_funcs import *
from utils import *
from fmath import *

def options_parse():
	"""
	Function to define arguments list for command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("filename",
						type=str,
						help="A name for input dataset")
	return parser.parse_args()

def pair_plot_scatter(ax, x, y):
	"""
	To plot scatter for one pair of courses
	"""
	colors = ['red', 'yellow', 'blue', 'green']
	for idx in range(len(x)):
		ax.scatter(x[idx], y[idx], s=1, color=colors[idx], alpha=0.5)

def pair_plot_hist(ax, X):
	"""
	To plot histogram for single course
	"""
	colors = ['red', 'yellow', 'blue', 'green']
	for idx in range(len(X)):
		ax.hist(X[idx][~np.isnan(X[idx])], color=colors[idx], alpha=0.5)

def pair_plot(houses, features, data_house):

	font = {'family' : 'DejaVu Sans',
			'weight' : 'light',
			'size'   : 7}
	plt.rc('font', **font)

	size = len(features) - 1
	_, ax = plt.subplots(nrows=size, ncols=size)
	plt.subplots_adjust(wspace=0.15, hspace=0.15)
	plt.gcf().canvas.set_window_title('Pair Plot')
	for row in range(size):
		for col in range(size):
			x, y = get_data_house_one_pair(data_house, houses, row + 1, col + 1)

			if col == row:
				pair_plot_hist(ax[row, col], x)
			else:
				pair_plot_scatter(ax[row, col], x, y)

			if ax[row, col].is_last_row():
				ax[row, col].set_xlabel(features[col + 1].replace(' ', '\n'))
			else:
				ax[row, col].tick_params(labelbottom=False)

			if ax[row, col].is_first_col():
				ax[row, col].set_ylabel(features[row + 1].replace(' ', '\n'))
			else:
				ax[row, col].tick_params(labelleft=False)

			ax[row, col].spines['right'].set_visible(False)
			ax[row, col].spines['top'].set_visible(False)

	plt.legend(houses, loc='center left', frameon=False, bbox_to_anchor=(1, 0.5))
	plt.show()

def do_main_function():
	"""
	Main function of PAIR_PLOT command in DSLR project
	"""
	args = options_parse()
	dataset = load_csv(args.filename)
	houses, features, data = preprocessing(dataset)
	data_house = get_data_house(data, houses)

	pair_plot(houses, features, data_house)

	"""
	v0
	data = dataset[1:, 6:]
	data = data[data[:, 1].argsort()]
	features = dataset[0, 6:]
	legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
	pair_plot(np.array(data, dtype=float), features, legend)
	plt.show()
	"""


if __name__ == '__main__':
	do_main_function()
