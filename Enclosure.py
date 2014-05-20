def Enclosure(Q):
	#q=[(x,y,width,height),(x,y,width,height)]
	tall=-10000000000000000000
	wide=-10000000000000000000
	smallx=10000000000000000
	smally=10000000000000000
	for i in range(len(Q)):
		if Q[i][1]+Q[i][3] > tall:
			tall=Q[i][1]+Q[i][3]
		if Q[i][0]+Q[i][2] > wide:
			wide=Q[i][0]+Q[i][2]
		if Q[i][0]<smallx:
			smallx=Q[i][0]
		if Q[i][1]<smally:
			smally=Q[i][1]
	finalh=tall-smally
	finalw=wide-smallx
	final=(smallx,smally,finalw,finalh)
	return final;
		