#!/usr/bin/env python3

import argparse

#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from stream_funcs import *
from utils import *
from fmath import *
from pandas.plotting import scatter_matrix


def do_main_function():
	"""
	Main function of HISTOGRAM command in DSLR project
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("filename", type=str, help="A name for input dataset")
	args = parser.parse_args()
	dataset = load_csv(args.filename)

	houses, features, data = preprocessing(dataset)
	print(features[1:])
	df_data = pd.DataFrame(data)
	print(df_data.loc[:,'1':'13'])

	_ = scatter_matrix(df_data.loc[:,'1':],
			figsize=(15,8),
			diagonal='kde',
			c='red',
			s=200,
			lw=3)

	"""
	for course in features[1:]:
		for house in houses:
			asset = data[course]
			print(asset)
	print(features)

	pd.DataFrame(data)
	"""

if __name__ == '__main__':
	do_main_function()


