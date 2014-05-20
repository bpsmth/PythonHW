def capitalize(x):
	wor=x
	fin=wor[0].upper()+wor[1:]
	return fin;
def title(x):
	work=x.split()
	senten=map(capitalize,work)
	final=" ".join(senten)
	return final;


