from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import numpy as np
import sklearn.decomposition as skd
import csv
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

#matrix = np.random.random((20,20))
#print matrix

matA=[]
with open('wighted_similarity.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	ko = []
    	for co in row:
    		ko.append(float(co))
    	matA.append(ko)

trsvd = skd.TruncatedSVD(n_components=100)
transformed = trsvd.fit_transform(matA)

user_list = []
row1 = []
popat = []
with open('user_vector_3.csv', 'rb') as f:
	reader = csv.reader(f)
	i=0
	for row in reader:
		j=0
		ko = []
		for co in row:
			if j==0 and i>0:
				user_list.append(co)
			if i==0:
				row1.append(co)
			j=j+1
		i=i+1
popat.append(row1[0:101])
o=0
for o in range(len(user_list)):
	goal = []
	goal.append(user_list[o])
	for co in transformed[o]:
		goal.append(co)
	popat.append(goal)

print "kola"
with open("SVD_mat.csv", "w") as g:
	a = csv.writer(g,delimiter=',')
	for row in popat:
		a.writerow(row)
		i=i+1
