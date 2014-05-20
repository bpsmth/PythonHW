def NextGray(T): #T is a tuple like: (1,0,0,0,0,0) 
	#convert gray code to binary in loop below
	copy = list(T)
	for i in range(len(copy)-1, 0, -1):
		tot=sum(copy[:i])%2
		if (tot)==1:
			if copy[i]==1:
				copy[i]=0
			if copy[i]==0:
				copy[i]=1
		else:
			copy[i]=copy[i]
	#print(copy)
	#copy is now in binary
	#must add 1 to the binary code below
	flag=0
	for i in range(len(copy)-1, 0, -1):
		if flag != 1:
			if copy[i-1]==0:
				copy[i-1]=1
				copy[i]=0
				flag=1
			else:
				copy[i]=0
		
	#copy should now be the next binary number
	#below goes from binary to gray
	for i in range(len(copy)-1, 0, -1):
		if copy[i-1] == 1:
			if copy[i]==1:
				copy[i]=0
			if copy[i]==0:
				copy[i]=1
	return tuple(copy);