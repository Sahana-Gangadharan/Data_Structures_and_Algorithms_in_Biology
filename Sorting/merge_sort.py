def merge(a,b):
	n=len(a)
	ctr = 0
	i = 0
	j = 0
	c = [0]*(2*n)
	while i<n and j<n:
		if a[i]<b[j]:
			c[ctr]=a[i]
			i+=1
			ctr+=1
		else:
			c[ctr]=b[j]
			j+=1
			ctr+=1
	if i==(n) and j<n:
		for k in range(j,n):
			for l in range(j,n-k-1):
				if b[l]>b[l+1]:
					b[l],b[l+1]= b[l+1], b[l]
	while i==n and j<n:
		c[ctr]=b[j]
		j+=1
		ctr+=1
	if j==(n) and i<n:
		for k in range(i,n):
			for l in range(i,n-k-1):
				if a[l]>a[l+1]:
					a[l],a[l+1]= a[l+1], a[l]
	while j==(n) and i<n:
		c[ctr]=a[i]
		i+=1
		ctr+=1
	print(c)
	return c

# a = [1, 30, 50, 700, 5000]
# b = [2, 15, 25, 6509, 10000]
# merge(a,b)

def mergeSort(arr):
	if len(arr)==1:
		return arr
	else:
		return merge(mergeSort(arr[:(len(arr)/2)]),mergeSort(arr[(len(arr)/2):]))

mergeSort([5,3,1,7,4,6,2,11])