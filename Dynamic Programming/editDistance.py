def editDistance(s,t):
	m = len(s)
	n = len(t)

	#Initialise the matrix
	c = [0]*(n+1)
	
	for i in range(0,n+1):
		c[i]=[0]*(m+1)

	for i in range(1,m+1):
		c[0][i]=i
	for i in range(1,n+1):
		c[i][0]=i

	#Assuming cost of deletion/insertion and substitution is the same and cost = 1. Cost of match = 0.

	for i in range(1,n+1):
		for j in range(1,m+1):
			p = c[i-1][j] + 1
			q = c[i][j-1] + 1
			if str(s[j-1])==str(t[i-1]):
				r = c[i-1][j-1]
			else:
				r = r = c[i-1][j-1] + 1
			c[i][j] = min(p,q,r)
			
	# print(c)
	print('Smallest edit distance = %d' %c[n][m])

s = 'application'
t = 'applicant'
editDistance(s,t)