def orthogonality(vec1,vec2):
	summing = 0
	l=len(vec1)
	while(l>0):
		l = l-1
		summing=summing + vec1[l]*vec2[l]
	if summing==0:
		print('the two vectors are orthogonal')
	else:
		print('the two vectors are not orthogonal')
