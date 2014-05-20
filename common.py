def common(a,b):
	result=[x for x in a if x in b]
	
	#the above creates a custom list by going over every entry in A and checking against list b
	#it only puts x in the list if x is in both a and b
	return result;
	