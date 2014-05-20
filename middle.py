def teardown(a):
	new=a[1:(len(a)-1)]
	if len(new)!=0:
		return new;
	else:
		return None;
def middle(x):
	work=x.split()
	
	final=map(teardown,work)
	
	finishh=[b for b in final if b != None]
	finale=" ".join(finishh)
	return finale;