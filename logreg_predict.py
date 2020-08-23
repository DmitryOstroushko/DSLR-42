#!/usr/bin/env python3

import sys
import argparse
import numpy as np
import pandas as pd
from collections import OrderedDict

from stream_funcs import *

def options_parse():
	"""
	Function to define arguments list for command line
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("dataset",
						type=str,
						help="A name for input dataset")
	parser.add_argument("thetas_file",
						type=str,
						help="A name for coeffs of LG")
	return parser.parse_args()

class MyLogisticRegressionClass(object):
	def __init__(self, alpha=5e-5, n_iter=30000):
		self.alpha = alpha
		self.n_iter = n_iter

	def _scaling(self, X):
		for i in range(len(X)):
			X[i] = ( X[i] - X.mean()) / X.std()
		return X

	def _processing(self, dataset):
		dataset = dataset.iloc[:,5:]
		dataset = dataset.dropna()
		ds_features = np.array(dataset)

		np.apply_along_axis(self._scaling, 0, ds_features)
		return ds_features

	def _predict_one(self, x, thetas):
		return max((x.dot(w), c) for w, c in thetas)[1]

	def predict(self, X, thetas):
		X = self._processing(X)
		return [self._predict_one(i, thetas) for i in np.insert(X, 0, 1, axis=1)]

def do_main_function():
	try:
		args = options_parse()
	except:
		error_message("Wrong type/value of command line arguments.")
		normal_message("See -h option")
		sys.exit(-1)
	dataset = pd.read_csv(args.dataset, index_col = "Index")
	thetas = np.load(args.thetas_file)
	lrc = MyLogisticRegressionClass()
	predicts = lrc.predict(dataset, thetas)
	houses = pd.DataFrame(OrderedDict({'Index':range(len(predicts)), 'Hogwarts House':predicts}))
	houses.to_csv('houses.csv', index=False)
	success_message("Predictions saved to houses.csv")

if __name__ == '__main__':
	do_main_function()
