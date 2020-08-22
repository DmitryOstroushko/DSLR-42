#!/usr/bin/env python3

import argparse
import numpy as np

from stream_funcs import *
from utils import load_csv
from fmath import *

def set_numerical_features(features, dataset):
	numerical_features = dict.fromkeys(features, True)
	for idx in range(0, len(features)):
		try:
			data = np.array(dataset[:, idx], dtype=float)
			data = data[~np.isnan(data)]
			if not data.any():
				raise Exception()
		except:
			numerical_features[features[idx]] = False
	return numerical_features

def describe_vertical(filename):
	function_list = {'Count': count_,
					'Mean': mean_,
					'Std': std_,
					'Min': min_,
					'25%': percentile_25_,
					'50%': percentile_50_,
					'75%': percentile_75_,
					'Max': max_}

	dataset = load_csv(filename)
	features = dataset[0]
	dataset = dataset[1:]
	numerical_features = set_numerical_features(features, dataset)
	width_col = max([len(feature) for feature in features if numerical_features[feature]])
	print(f'{"":15}', end = '')
	for feature in features:
		if numerical_features[feature]:
			print(f' |{feature:12.12}', end = '')
	print()

	for function in function_list:
		print(f'{function:15}', end = '')
		for idx in range(len(features)):
			if numerical_features[features[idx]]:
				data = np.array(dataset[:, idx], dtype=float)
				data = data[~np.isnan(data)]
				print(f' |{function_list[function](data):>12.4f}', end = '')
		print()

def describe_horizontal(filename):
	dataset = load_csv(filename)
	features = dataset[0]
	dataset = dataset[1:]
	print(f'{"":15} |{"Count":>12} |{"Mean":>12} |{"Std":>12} |{"Min":>12} |{"25%":>12} |{"50%":>12} |{"75%":>12} |{"Max":>12}')
	for i in range(0, len(features)):
		print(f'{features[i]:15.15}', end=' |')
		try:
			data = np.array(dataset[:, i], dtype=float)
			data = data[~np.isnan(data)]
			if not data.any():
				raise Exception()
			print(f'{count_(data):>12.4f}', end=' |')
			print(f'{mean_(data):>12.4f}', end=' |')
			print(f'{std_(data):>12.4f}', end=' |')
			print(f'{min_(data):>12.4f}', end=' |')
			print(f'{percentile_(data, 25):>12.4f}', end=' |')
			print(f'{percentile_(data, 50):>12.4f}', end=' |')
			print(f'{percentile_(data, 75):>12.4f}', end=' |')
			print(f'{max_(data):>12.4f}')
		except:
			print(f'{count_(dataset[:, i]):>12.4f}', end=' |')
			print(f'{"No numerical value to display":>60}')

def do_main_function():
	"""
	Main function of DESCRIBE command in DSLR project
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", type=str, help="A name for input dataset")
	parser.add_argument("--print_mode",
						"-p",
						action="store",
						dest="print_mode",
						default="v",
						help="To print horizontally: h, vertically: v")

	args = parser.parse_args()
	if args.print_mode == 'v':
		describe_vertical(args.filename)
	elif args.print_mode == 'h':
		describe_horizontal(args.filename)
	else:
		error_message("Wrong print mode: use 'h' (horizontal) or 'v' (vertical)")

if __name__ == '__main__':
	do_main_function()
