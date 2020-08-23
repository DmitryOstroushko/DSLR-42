import sys
import numpy as np
import csv
from stream_funcs import *

def load_csv(filename):
	dataset = []
	try:
		with open(filename) as csv_file:
			reader = csv.reader(csv_file)
			for value_list in reader:
				row = []
				for value in value_list:
					try:
						value = float(value)
					except:
						if not value:
							value = np.nan
					row.append(value)
				dataset.append(row)
	except:
		error_message(f'file {filename}: {sys.exc_info()[1]}')
		sys.exit(1)
	return np.array(dataset, dtype=object)

def preprocessing(dataset):
	data = np.delete(dataset, 0, axis = 1)
	data = np.delete(data, [1,2,3,4], axis = 1)
	features = data[0]
	data = data[1:, :]
	houses = list(dict.fromkeys(data[:, 0]))
	# отсортировали по первому столбцу
	# data = data[data[:, 1].argsort()]
	return sorted(houses), features, data

def get_data_house(data, houses):
	"""
	To split data between houses
	"""
	data_house = []
	for idx_house in range(len(houses)):
		data_house.append(data[data[:,0] == houses[idx_house]])
	return data_house

def get_data_house_one_pair(data_house, houses, idx_1, idx_2):
	"""
	To get data for one pair features
	"""
	x = []
	y = []
	for idx_house in range(len(houses)):
		d = data_house[idx_house]
		x.append(np.array(d[:, idx_1], dtype=float))
		y.append(np.array(d[:, idx_2], dtype=float))
	return x, y
