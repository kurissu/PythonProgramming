def transpose(matrix):
	row=len(A)
	col=len(A[0])
	temp = []
	colElement = [0]*col
	matrix1 = [colElement]*row
	for i in range(row):
		for j in range(col):
			print(matrix[j][i],end='')
			matrix1[i][j] = matrix[j][i]
		print(' ')
	
		return temp

def multiply(X,Y):
	result = []
	# iterate through rows of X
	for i in range(len(X)):
	   # iterate through columns of Y
		rvec=[]
		for j in range(len(Y[0])):
	       # iterate through rows of Y
			#for k in range(len(Y)):
			rvec.append(X[i][k] * Y[k][j])
		result.append(rvec)
	for r in result:
		print(r)	

A = [[1,2,5]]
B = [[1],[2],[5]]
#B = transpose(A)
multiply(A,B)
