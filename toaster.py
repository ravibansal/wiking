from collections import defaultdict

fdd = defaultdict(list)
fdd["kola"] = 3
fdd["koea"] = 8
fdd["kowa"] = 5
fdd["koewa"] = 1

for w in sorted(fdd, key=fdd.get, reverse=True):
	print w, fdd[w]