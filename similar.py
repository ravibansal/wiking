import urllib2
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
import requests
from multiprocessing import Process
import fcntl
import sys
import os
import signal
from os import listdir
import time
import sys

def kola(stringname1,stringname2,back1,back2,idd1,idd2):
    base = "http://wikipedia-miner.cms.waikato.ac.nz/services/compare?term1="
    hui=0
    popat=0
    s = requests.Session()
    s.proxies = {"http": "http://10.3.100.207:80"}
    o=base+stringname1+"&term2="+stringname2
    r = s.get(o)
    soup = BeautifulSoup(r.text,"html.parser")
    tags = soup.findAll('message')
    for tag1 in tags:
        popat = tag1['relatedness']
    if popat == 0:
        o=base+back1+"&term2="+back2
        r = s.get(o)
        soup = BeautifulSoup(r.text,"html.parser")
        tags = soup.findAll('message')
        for tag1 in tags:
            popat = tag1['relatedness']
    #print stringname1,stringname2,popat
    myCsvRow = []
    myCsvRow.append(idd1)
    myCsvRow.append(idd2)
    myCsvRow.append(str(popat))
    filee = "/usr2/sdf/wiking/crawl/pyscript/collec/parallel_"+idd1+"_"+idd2+".csv"
    with open(filee, "w") as g:
        a = csv.writer(g,delimiter=',')
        a.writerow(myCsvRow)
    g.close()


l = ""
m = ""
k = "http://wikipedia-miner.cms.waikato.ac.nz/services/compare?term1="
pq=0
rs=0
matrixX = []
moly = {}

c1 = []
c2 = []
idd = []
t=0
with open('selected_new_pages1.csv', 'rb') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        if i > 100:
            break
        t=t+1
        c1.append(row[1])
        c2.append(row[2])
        idd.append(row[0])

i=0
proc = []
for i in range(t):
    pq = pq+1
    rowX = []
    l=c1[i]
    l1=c2[i]
    l.replace (" ", "%20")
    l1.replace (" ", "%20")
    flag=0
    j=i+1
    for j in range(t):
        popat = 0
        if j%1000 == 0 or j==i+1:
            print c1[i],c1[j],"working",len(proc)
        hui = 0
        m=c1[j]
        m1=c2[j]
        m.replace (" ", "%20")
        m1.replace (" ", "%20")
        p = Process(target=kola,args=(l,m,l1,m1,idd[i],idd[j]))
        p.daemon = True
        p.start()
        proc.append(p)
        if len(proc) > 1000:
            for pe in proc:
                pidd = pe.pid
                try:
                    os.kill(pidd, signal.SIGTERM)
                except OSError:
                    kola1=1
                #pe.terminate()
            proc = []

for p in proc:
    p.join()

i=0