def subzero(x):
	small=min(x)
	def foo(x):
		if x == small:
			return 0;
		else:
			return x;
	result=map(foo, x)
	return result;