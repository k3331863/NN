import csv
from io import StringIO
import numpy as np
from itertools import islice

# def update(input):
	# aH = []
	# aO = []
	# for index in range(nh):
	# 	aH = np.tanh(input * wI)
	# aH = np.array(aH).reshape(nh)
	# for index in range(no):
	# 	aO = np.tanh(aH * wO)
	# aO = np.array(aO).reshape(no)


def test(testFile, weightFile):
	hidden = 57
	feature_num = 57
	# with open('ansNN.csv', 'w', newline='') as out:
	with open('ansNN.csv', 'wb') as out:
		reader = csv.reader(open(testFile,'r'))
		writer = csv.writer(out, delimiter = ',')

		wI = np.matrix(np.zeros(shape = (feature_num, hidden)))
		wO = np.matrix(np.zeros(shape = (hidden, 1)))


		f = open("nnZ.txt", "w")
		m = open(weightFile, 'r')

		i = 0
		for line in m.readlines():
			line = line.strip().split(' ')
			if i < feature_num:
				wI[i] = [float(val) for val in line]
				i += 1
			else:
				wO[0] = [float(val) for val in line]

		# print wI

		writer.writerow(["id", "label"])
		row = [0, 0]
		data = np.ones(feature_num)
		aH = np.zeros(hidden)
		aO = np.zeros(1)
		for case in reader:
			row[0] = str(case[0])
			# data[1:] = np.asarray([float(val) for val in case[1:]])
			data[:] = np.asarray([float(val) for val in case[1:]])

			# break
			# aH = 1/ (1+ np.exp(-1*(data*wI)))
			# aO = 1/ (1+ np.exp(-1*np.sum(wO*aH)))
			# print data * wI

			aH = np.tanh((data * wI))
			aO = np.tanh(np.sum(aH*wO))

			f.write(str(aO)+'\n')
			if aO > 0.5:
				row[1] = "1"
			else:
				row[1] = "0"
			writer.writerow(row)

		f.close()

def main():
	test("./spam_data/spam_test.csv", "nnModel.txt")

if __name__ == "__main__":
	main()
