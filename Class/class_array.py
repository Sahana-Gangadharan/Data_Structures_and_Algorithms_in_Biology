class array:
	def __init__(self, array):
		n = len(array)
		for i in range(n):
			self[i]=array[i]

	def sort(self):
		n = len(self)
		for i in range(n):
			for j in range(1,i+1):
				if self[j]<self[i]:
					self[i], self[j] = self[j], self[i]
		return self

	def _search(self,element):
		n = len(self)
		for i in range(n):
			if element == self[i]:
				return True
			else:
				return False

	def _insert(self,element):
		n = len(self)
		for i in range(n):
			if element < self[i]:
				ctr = i

		self = self[:i] + element + self[i:]

a = [1, 3, 2, 14, 7, 5, 18, 9]
b = array(a)
b.sort()
b._search(2)
