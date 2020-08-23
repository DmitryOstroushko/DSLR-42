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
	#colors = ['green', 'yellow', 'red', 'blue']
	colors = [plt.cm.tab10(i/float(len(legend)-1)) for i in range(len(legend))]

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

def get_similiar_pairs(data, n):
	similar_features = []
	for idx in range(0, n):
#		print(type(data[idx]))
		a = np.array(data[idx], dtype=float)
		for idx_vs in range(idx + 1, n):
			b = np.array(data[idx_vs], dtype=float)
#			np.polyfit(a, b, 1)
#			a = np.array(data[idx], data[idx_vs])
#			c = np.corrcoef(a)
#			print(f'idx = {idx}, idx_vs = {idx_vs}, m = {m}, b = {b}')


#			is_similiar = True
#			koeff = 0
#			shift = 0
#			for row in range(len(data[idx])):
#				if row == 0:
#					shift = data[idx_vs][data[idx_vs][0] == 0]
#
#					koeff = data[idx][row] / data[idx_vs][row]
#				#if idx == 2 and idx_vs == 4:
#				#	print(data[idx][row], data[idx_vs][row])
#				#	print(shift)
#				#	print('div ' + str(data[idx][row] / data[idx_vs][row]))
#				if data[idx][row] == data[idx_vs][row] or data[idx][row] == 0 or data[idx_vs][row] == 0:
#					continue
#				if data[idx][row] / data[idx_vs][row] != koeff:
#					#if idx == 2 and idx_vs == 4:
#					#	print('koeff ' + str(koeff))
#					#	print('div ' + str(data[idx][row] / data[idx_vs][row]))
#
#					is_similiar = False
#					break
#			if is_similiar:
#				similar_features.append([idx, idx_vs])
#	return similar_features

def do_main_function():
	"""
	Main function of SCATTER_PLOT command in DSLR project
	"""
	args = options_parse()
	dataset = load_csv(args.filename)
	houses, features, data = preprocessing(dataset)
	data_house = get_data_house(data, houses)

	plt.gcf().canvas.set_window_title('Scatter Matrix')

	similar_features = get_similiar_pairs(data[:, 1:], len(features))
#	print(similar_features)

	if args.print_all:
		plt.text(0.05, 0.5, 'ATTENTION!\nPLEASE WRITE DOWN\nNUMBERS OF SIMILIAR FEATURES',
			fontsize = 20)
		plt.show()
		for idx in range(1, len(features)):
			for idx_vs in range(idx + 1, len(features)):
				plt.gcf().canvas.set_window_title('Scatter Matrix')
				calc_and_plot(houses, features, data_house, idx, idx_vs)

	plt.gcf().canvas.set_window_title('The similiar features')
	if similar_features and len(similar_features):
		print('The similiar features are:')
		for pair in similar_features:
			print(f'{features[pair[0]]} and {features[pair[1]]}')
			plt.gcf().canvas.set_window_title('The similiar features')
			calc_and_plot(houses, features, data_house, pair[0], pair[1])
	else:
		feature_1 = input('Input number of 1st feature: ')
		feature_2 = input('Input number of 2nd feature: ')
		try:
			calc_and_plot(houses, features, data_house, int(feature_1), int(feature_2))
		except:
			print(sys.exc_info()[1])
			print("You should input int values in range 1 - " + str(len(features) - 1))

if __name__ == '__main__':
	do_main_function()
