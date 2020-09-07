def selectionSort(array):
	n= len(array)
	ctr= 0
	for i in range(n):
		check = i
		for j in range(i+1,n):
			if array[j]<array[check]:
				check = j
		array[i], array[check] = array[check], array[i]
		ctr+=1
		print(array)

	print(array)
	print(ctr)

array = [6,10,4,5,1,2]
selectionSort(array)