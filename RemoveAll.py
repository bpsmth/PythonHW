def RemoveAll(D,limit):
	keys=D.keys()
	for a in keys:
		if D[a]>limit:
			del D[a]