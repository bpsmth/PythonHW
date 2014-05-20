def Findex(G):
	result={}
	for (v,text) in G:
		work=text.split()
		for word in work:
			if word not in result:
				result[word]=[v]
			if v not in result[word]:
				result[word].append( v )			
	return result;