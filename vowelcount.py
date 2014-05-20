def vnum(x):
	letter=x.split()
	vowels="aeiou"
	final=[letters[i] in range(len(letters)-1) if letters[i] in vowels]
	total=sum(final)
	return letter;
def vowelcount(y):
	working=y
	result=map(vnum,working)
	return result;





