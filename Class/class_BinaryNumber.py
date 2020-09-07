# Roll number - BE17B038
# Name - Sahana
# PopQuiz 1

class BinaryNumber():
	def __init__(self, array):
		n= len(array)
        for i in range(n):
            if array[i]!=0 or array[i]!=1:
            raise ValueError('Check your input!')
			self._data[i]=array[i]

	def __repr__(self):
		a=0
		n=len(self)
		for i in range(n):
			a+=self._data[i]*(10**i)
		return '['+ str(int(a)) + ']_2'

	def value(self):
		value = 0
		n = len(self)
		for i in range(n):
			value+=self._data[i]*(2**i)
		return value

b1 = BinaryNumber([0,1,1,1])
b2 = BinaryNumber([0,0,0,1])
print(b1)
print(b2)
print(b1.value()+b2.value())
b3= BinaryNumber([0,1,1,2])

