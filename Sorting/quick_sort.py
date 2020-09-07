def quickSort(a):
	'''Quick Sort in place'''

	n=len(a)
	swap=0
	pivot=n-1
	# left=[]
	# right=[]
	# for i in range(n-1):
	# 	if a[i]<a[pivot]:
	# 		left.append(a[i])
	# 	else:
	# 		right.append(a[i])

	for i in range(n):
		for j in range(n-i):
			if a[j]>a[pivot]:
				a[j],a[pivot]=a[pivot],a[j]
				swap+=1
		pivot-=1
	print(swap)
	print(a)

def pivotSplit(a):
	n=len(a)
	pivot=n-1
	left=[]
	right=[]
	for i in range(n-1):
		if a[i]<a[pivot]:
			left.append(a[i])
		else:
			right.append(a[i])
	return left,right

def QuickSort(a):
	n=len(a)
	if n<2:
		return
	final=[]
	final.append(pivotSplit(a))
	

a = [6,10,4,5,1,2]
quickSort(a)