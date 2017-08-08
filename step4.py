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

#print transformed
similarity_matrix = cosine_similarity(matA,matA)
print "similarity_matrix ",len(similarity_matrix),len(similarity_matrix[0])
#print VT

if len(similarity_matrix)!=11705:
	print "Dimension error"
else:
	user_list = []
	user_pages = []
	pages_list = []
	with open('user_vector_3.csv', 'rb') as f:
		reader = csv.reader(f)
		i=0
		for row in reader:
			j=0
			ko = []
			for co in row:
				if j==0 and i>0:
					user_list.append(co)
				if j>0 and i>0:
					ko.append(float(co))
				if i==0 and j>0:
					pages_list.append(co)
				j=j+1
			if i > 0:
				user_pages.append(ko)
			i=i+1
	print "user_list ",len(user_list)
	print "pages_list ",len(pages_list)
	print "user_pages ",len(user_pages),len(user_pages[0])
	predic = defaultdict(list)
	i=0
	for i in range(len(user_list)):
		num_suggested=0
		user_chosen=0
		chosen = []
		predic[user_list[i]].append(user_list[i])
		while num_suggested < 10:
			j=0
			mad_max = 0
			ind = -1
			for j in range(len(user_list)):
				if similarity_matrix[i][j] > mad_max and user_list[j] not in chosen:
					mad_max = similarity_matrix[i][j]
					ind = j
					chosen.append(user_list[j])
			j=0
			if ind != -1:
				user_chosen=user_chosen+1
				for j in range(len(pages_list)):
					if user_pages[ind][j] > 0 and user_pages[i][j] == 0:
						predic[user_list[i]].append(pages_list[j])
						num_suggested=num_suggested+1
			else:
				break
	print "poker"
	with open("recommend_4.csv", "w") as g:
		a = csv.writer(g,delimiter=',')
		for key in predic:
			a.writerow(predic[key])
