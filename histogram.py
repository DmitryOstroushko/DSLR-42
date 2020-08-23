#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

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
						help='If set, drawing histograms for all courses')
	return parser.parse_args()

def plot_histogram(X, legend, title, xlabel, ylabel):
	"""
	To plot histogram for single course
	"""
	colors = ['green', 'yellow', 'red', 'blue']
	#colors = [plt.cm.tab10(i/float(len(legend)-1)) for i in range(len(legend))]
	for idx in range(len(X)):
		plt.hist(X[idx][~np.isnan(X[idx])], color=colors[idx], alpha=0.5)
	plt.legend(legend, loc='upper right', frameon=False)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()

def calc_and_plot(houses, features, data_house, idx):
	"""
	To calc and plot histogram for one course
	"""
	data_col = []
	for idx_house in range(len(houses)):
		d = data_house[idx_house]
		data_col.append(np.array(d[:, idx], dtype=float))
	plot_histogram(data_col, legend=houses, title=features[idx], xlabel='Marks', ylabel='A number of students')

def do_main_function():
	"""
	Main function of HISTOGRAM command in DSLR project
	"""
	args = options_parse()
	dataset = load_csv(args.filename)
	houses, features, data = preprocessing(dataset)
	data_house = get_data_house(data, houses)

	mark_range = []

	min_mark_range = np.inf
	idx_homogeneous_feature = 0

	for idx in range(1,len(features)):
		mark_1 = np.array(data[:, idx], dtype=float)
		if (max(mark_1) - min(mark_1)) < min_mark_range:
			min_mark_range = max(mark_1) - min(mark_1)
			idx_homogeneous_feature = idx
		if args.print_all:
			plt.gcf().canvas.set_window_title('Score distribution')
			calc_and_plot(houses, features, data_house, idx)

	print(f'The most homogeneous score: course = {features[idx_homogeneous_feature]}, marks range = {min_mark_range:.2f}')
	plt.gcf().canvas.set_window_title('The most homogeneous score')
	calc_and_plot(houses, features, data_house, idx_homogeneous_feature)

if __name__ == '__main__':
	do_main_function()
