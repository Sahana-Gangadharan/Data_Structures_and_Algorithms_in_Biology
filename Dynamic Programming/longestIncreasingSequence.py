def lis(array):
	n = len(array)
	l = []
	count = []
	ar = []
	ctr=0
	for i in range(n):
		ar.append(array[i])
		ctr+=1
		for k in range(i,n):
			for j in range(k,n):
				if array[k]>ar[ctr-1]:
					ar.append(array[k])
					ctr+=1
			count.append(ctr)
			print(ar)
			print(ctr)
		ctr=0
		ar=[]
	# print(count)
	# print(max(count))

a = [1,5,3,6,2,7,8,4,9]
lis(a)
