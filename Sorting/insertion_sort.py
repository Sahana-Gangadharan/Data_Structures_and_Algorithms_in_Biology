def insertionSort(n,ar):
	# n=len(ar)
	swap= 0

	for i in range(n-1):
		value=ar[i+1]
		k=i
		while k>=0 and value<ar[k]:
			ar[k+1]=ar[k]
			k=k-1
		swap+=1
		ar[k+1]=value
		print(ar)
	print(swap)

	print(ar)

# def insertionSort(n,ar):
# 	n = len(ar)
# 	swap=0
# 	for i in range(1,n):
# 		for j in range(i,0,-1):
# 			if ar[j]<ar[j-1]:
# 				ar[j-1],ar[j]=ar[j],ar[j-1]
# 				swap+=1
# 	print(swap)
# 	print(ar)


array = [11,1,6,3,9,17,4,9,2,8,30,25]
ar = [6,10, 4, 5, 1, 2]
insertionSort(6,ar)