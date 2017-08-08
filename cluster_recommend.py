import csv 
from collections import defaultdict

cluster = defaultdict(list)
with open('cluster_data.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		cluster[row[102]].append(row[1])

actual = defaultdict(list)
pageid = []
with open('user_page_matrix_single.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	j=0
    	idd = ""
    	for co in row:
    		if j==0:
    			idd = co
    		if j>0:
    			actual[idd].append(co)
    		j=j+1

predic = defaultdict(list)

for clus in cluster:
	pq = defaultdict(list)
	for peop in cluster[clus]:
		i=0
		for page in actual[peop]:
			if page in pq:
				pq[page] = pq[page] +1
			else:
				pq[page] = 0
			i=i+1

	for peop in cluster[clus]:
		i = 0
		for kq in sorted(pq, key=pq.get, reverse=True):
			if peop not in predic:
				predic[peop].append(peop)
			if kq not in actual[peop]:
				predic[peop].append(kq)
			if len(predic[peop]) > 10:
				break
			i=i+1

print "poker"
with open("recommend_cluster.csv", "w") as g:
	a = csv.writer(g,delimiter=',')
	for key in predic:
		a.writerow(predic[key])