def Smooth(a,Threshold):
	flag=0
	for i in range(len(a)-1):
		con=abs((a[i]-a[i+1]))
		if con > Threshold and flag!=1:
			avg=(a[i]+a[i+1])/2
			a.insert(i+1,avg)
			flag=1
			