def determinant(x):
	#this function returns the value of the determinant for a 2x2 matrix
	det=(x[0][0]*x[1][1])-(x[0][1]*x[1][0])
	#above statement calculates the det from the values passed in
	#below statement returns the calculation
	return det;
	
#these two statements were used for testing	
#A = [ [23.0,19.2], [-5.1,45.8] ]
#print(determinant(A))