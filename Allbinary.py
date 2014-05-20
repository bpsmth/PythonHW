def Allbinary(N):
	final=[]
	work=worker(N)
	#print(len(work))
	for i in range (len(work)):
		#print(i)
		#new=int(work[i])
		results=[]
		for ii in range(len(work[i])):
			numbr=int(work[i][ii])
			results.append(numbr)
		c=tuple(results)
		final.append(c)
		finale=tuple(final)
	return finale;
def worker(N):
	if N==1:
		return ['0','1'];
	else:
		branch1= ['0' + x for x in worker(N-1)]
		branch2= ['1' + x for x in worker(N-1)]
		return branch1+branch2;