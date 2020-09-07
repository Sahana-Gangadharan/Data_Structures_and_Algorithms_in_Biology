class queue_array():
	''' Class queue Array
	'''
	default_capacity = 10

	def __init__(self):
		self._front=0
		self._size = 0
		self._elements = []*queue_array.default_capacity

	def length(self):
		return len(self._size)

	def isEmpty(self):
		return len(self._elements)==0

	def enqueue(self,value):
		if len(self._elements)== self._size:
			self._resize(2*queue_array.default_capacity)
		add = (self._front+ self._size)% len(self._elements)
		self._elements[add]=value
		self._size+=1

	def show(self):
		print(self._elements)

	def front(self):
		if self.isEmpty():
			raise EmptyError('Queue is empty!')
		return self._elements[self._front]

	def dequeue(self):
		if self.isEmpty():
			raise EmptyError('Queue is empty!')
		else:
			first = self._elements[self._front]
			self._elements[self._front] = None
			self._front = (self._front + 1)% len(self._elements)
			self._size-=1
			return first

	def _resize(self,qty):
		old= self._elements
		self._elements=[None]*qty
		walk = self._front
		for k in range(self._size):
			self._elements[k]=old[k]
			walk = (1+walk)%len(old)
		self._front=0

def queue_Array():
	a = queue_array()
	
	element1 = input("Enter element to initialise the queue - ")
	a.enqueue(element1)

	print("Do you want to continue? Enter Y/N - ")
	decide = str(input())

	while decide == 'Y' or decide == 'y':

		print("Which of the following tasks do you want to do?\n1.Enqueue\n2.Dequeue\n3.First element\n")
		option = int(input("Enter number : "))
		if option==1:
			element = input("Enter element to enqueue - ")
			a.enqueue(element)
		elif option==2:
			a.dequeue()
		elif option==3:
			a.front()
		else:
			print("Sorry! Wrong option.\n")
			return
		a.show()
		print("Do you want to continue? Enter Y/N - ")
		decide = str(input())

	while decide == 'N' or decide == 'n':

		print("See ya next time!\n")
		return

queue_Array()