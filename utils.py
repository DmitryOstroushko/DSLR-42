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

