import numpy as np
import csv

def load_csv(filename):
	dataset = []
	with open(filename) as csv_file:
		reader = csv.reader(csv_file)
		try:
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
			print(f'file {filename}, line {reader.line_num}: {e}')
	return np.array(dataset, dtype=object)
	#return dataset
