def bubbleSort(array):
	n=len(array)
	ctr=0
	for i in range(n):
		for j in range(n-i-1):
			if array[j]>array[j+1]:
				array[j],array[j+1]= array[j+1], array[j]
				ctr+=1
			print(array)
	print(array)
	print(ctr)

array = [6,10,4,5,1,2]
bubbleSort(array)