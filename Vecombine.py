def Vecombine(A,B,C):
	result=1.0
	for i in range(len(A)):
		A[i]=A[i]*B[i]+C[i]
		if A[i]<0:
			result=-1.0
	return result;