#!/usr/bin/env python3

import argparse
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

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
	parser.add_argument('--print_all', '-p',
						action="store_true",
						dest="print_all",
						default=False,
						help='If set, drawing scatter for all pairs of courses')
	return parser.parse_args()

def plot_scatter(x, y, legend, title, xlabel, ylabel):
	"""
	To plot scatter for one pair of courses
	"""
	colors = ['green', 'yellow', 'red', 'blue']
	for idx in range(len(x)):
		plt.scatter(x[idx], y[idx], color=colors[idx], alpha=0.5)
	plt.legend(legend, loc='upper right', frameon=False)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()

def calc_and_plot(houses, features, data_house, idx, idx_vs):
	"""
	To calc and plot scatter plot for one pair of courses
	"""
	x = []
	y = []
	for idx_house in range(len(houses)):
		d = data_house[idx_house]
		x.append(np.array(d[:, idx], dtype=float))
		y.append(np.array(d[:, idx_vs], dtype=float))
	plot_scatter(x, y, legend=houses, title=features[idx] + "(" + str(idx) + ") vs " + features[idx_vs] + "(" + str(idx_vs) + ")", xlabel=features[idx], ylabel=features[idx_vs])

def do_main_function():
	"""
	Main function of SCATTER_PLOT command in DSLR project
	"""
	args = options_parse()
	dataset = load_csv(args.filename)
	houses, features, data = preprocessing(dataset)
	data_house = get_data_house(data, houses)

	plt.gcf().canvas.set_window_title('Scatter Matrix')

	if args.print_all:
		plt.text(0.05, 0.5, 'ATTENTION!\nPLEASE WRITE DOWN\nNUMBERS OF SIMILIAR FEATURES',
			fontsize = 20)
		plt.show()
		for idx in range(1, len(features)):
			for idx_vs in range(idx + 1, len(features)):
				plt.gcf().canvas.set_window_title('Scatter Matrix')
				calc_and_plot(houses, features, data_house, idx, idx_vs)

	print('The similiar features are:')
	feature_1 = input('Input number of 1st feature: ')
	feature_2 = input('Input number of 2nd feature: ')

	plt.gcf().canvas.set_window_title('The similiar features')
	calc_and_plot(houses, features, data_house, int(feature_1), int(feature_2))

	#for pair in similar_features:
	#	print(f'{features[pair[0]]} and {features[pair[1]]}')
	#	plt.gcf().canvas.set_window_title('The similiar features')
	#	calc_and_plot(houses, features, data_house, pair[0], pair[1])

if __name__ == '__main__':
	do_main_function()
