def sucontain(working):
		work=working.split()
		result=[work[i] in work[i+1] for i in range(len(work)-1)]
		finale=zip( work, result )
		res=[finale[i][0] for i in range(len(finale)) if finale[i][1]==True]
		return res;	