def substitute(x):
	if x[0].isdigit():
		answer = float(x)
		return answer;
	else:
		answerb = x
		return answerb;
def convert(x):
	splitstring=x.split(",")
	result=map(substitute,splitstring)
	final=tuple(result)
	return final;