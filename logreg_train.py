#!/usr/bin/env python3

import sys
import argparse
import numpy as np
import pandas as pd

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
	parser.add_argument('-a', '--alpha',
						dest="alpha",
						type=int,
						action="store",
						help="alpha parameter")
	parser.add_argument('-n', '--n_iter',
						dest="n_iter",
						type=int,
						action="store",
						help="A number of iterations")
	return parser.parse_args()


class MyLogisticRegressionClass(object):
	def __init__(self, thetas=[], alpha=5e-5, n_iter=30000):
		self.alpha = alpha
		self.n_iter = n_iter
		self.thetas = thetas

	def _scaling(self, X):
		for idx in range(len(X)):
			X[idx] = (X[idx] - X.mean())/X.std()
		return X

	def _processing(self, dataset):
		dataset = dataset.dropna()
		ds_features = np.array((dataset.iloc[:,5:]))
		ds_labels = np.array(dataset.loc[:,"Hogwarts House"])
		np.apply_along_axis(self._scaling, 0, ds_features)
		return ds_features, ds_labels

	def _sigmoid(self, x):
		return 1 / (1 + np.exp(-x))

	def fit(self, dataset):
		X, y = self._processing(dataset)
		X = np.insert(X, 0, 1, axis=1)
		m = X.shape[0]

		for house in np.unique(y):
			y_copy = np.where(y == house, 1, 0)
			thetas = np.ones(X.shape[1])

			for _ in range(self.n_iter):
				output = X.dot(thetas)
				errors = y_copy - self._sigmoid(output)
				gradient = np.dot(X.T, errors)
				thetas += self.alpha * gradient
			self.thetas.append((thetas, house))
		return self.thetas

	def _predict_one(self, x):
		return max((x.dot(w), c) for w, c in self.thetas)[1]

	def predict(self, X):
		return [self._predict_one(item) for item in np.insert(X, 0, 1, axis=1)]

	def score(self, dataset):
		X, y = self._processing(dataset)
		return sum(self.predict(X) == y) / len(y)

def save_thetas(thetas, file_name):
	try:
		np.save(file_name, thetas)
	except:
		error_message(str(sys.exc_info()[1].args[1]))
		error_message('It is impossible to save theta values')

def do_main_function():
	try:
		args = options_parse()
	except:
		error_message("Wrong type/value of command line arguments.")
		normal_message("See -h option")
		sys.exit(-1)
	dataset = pd.read_csv(args.dataset, index_col = "Index")
	lrc = MyLogisticRegressionClass()
	thetas = lrc.fit(dataset)
	save_thetas(thetas, args.thetas_file)
	success_message("Coeffs array is saved to " + args.thetas_file)
	normal_message("Score = " + str(lrc.score(dataset)))

if __name__ == '__main__':
	do_main_function()
