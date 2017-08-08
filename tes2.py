import csv
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
iris = []
with open('small.csv', 'rb') as f:
	data = csv.reader(f)
	for row in data:
		iris.append(row)	
pole = ['a','b','c','d']
print(iris)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
     iris,pole, test_size=0.4, random_state=0)
print(X_train.shape, y_train.shape)