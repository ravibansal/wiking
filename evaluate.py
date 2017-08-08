import csv
from collections import defaultdict

actual = defaultdict(list)
with open('user_page_matrix_act2014.csv', 'rb') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
    	j=0
    	idd=""
    	for co in row:
    		if j==0 and i>0:
    			idd = co
    		if j>0 and i>0:
    			actual[idd].append(co)
    		j=j+1
    	i=i+1
eval_r = defaultdict(list)
result = 0.0
user_num = 0.0
with open('recommend_4.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	user_num = user_num+1.0
    	j=0
    	idd=""
    	succ = 0.0
    	fai = 0.0
    	flog=0
    	num_rec = 0
    	for co in row:
    		if j==0:
    			idd = co
    			if idd in actual:
    				flog = 1
    		else:
    			num_rec = num_rec+1
    			if co in actual[idd]:
    				succ = succ+1.0
    			else:
    				fai = fai+1.0
    		if flog == 0:
    			break
    		j=j+1
    	if flog == 1:
    		if succ > 10:
    			eval_r[idd] = 1.0
    		else:
    			eval_r[idd] = (succ/(fai+succ))
	    	result = result+eval_r[idd]
result = result/user_num
print result
