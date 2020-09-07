class priorityQueue_array():
	''' Class queue Array
	'''
	default_capacity = 2

	def __init__(self):
		self._front=0
		self._size = 0
		self._priority = []*priorityQueue_array.default_capacity
		self._elements = []*priorityQueue_array.default_capacity

	def length(self):
		return len(self._size)

	def isEmpty(self):
		return len(self._elements)==0

	def enqueue(self,value,priority):
		if len(self._elements)== self._size:
			self._resize(2*priorityQueue_array.default_capacity)
		add = (self._front+ self._size)% len(self._elements)
		self._elements[add]=value
		self._priority[add]=priority
		self._size+=1

	def show(self):
		print(self._elements)

	def front(self):
		if self.isEmpty():
			raise ValueError('Queue is empty!')
		return self._elements[self._front]

	def dequeue(self):
		if self.isEmpty():
			raise ValueError('Queue is empty!')
		else:
			dele = self._priority.index(max(self._priority))
			first = self._elements[dele]
			self._elements.remove(self._elements[dele])
			self._priority.remove(self._priority[dele])
			self._size-=1
			return first

	def _resize(self,qty):
		old= self._elements
		oldp= self._priority
		self._elements=[None]*qty
		self._priority=[None]*qty
		walk = self._front
		for k in range(self._size):
			self._elements[k]=old[k]
			self._priority[k]=oldp[k]
			walk = (1+walk)%len(old)
		self._front=0

def priorityQueue_Array():
	a = priorityQueue_array()
	
	element1, priority1 = input("Enter element to initialise the queue - ").split()
	a.enqueue(element1,priority1)

	print("Do you want to continue? Enter Y/N - ")
	decide = str(input())

	while decide == 'Y' or decide == 'y':

		print("Which of the following tasks do you want to do?\n1.Enqueue\n2.Dequeue\n3.First element\n")
		option = int(input("Enter number : "))
		if option==1:
			element, priority = input("Enter element to enqueue - ").split()
			a.enqueue(element,priority)
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

priorityQueue_Array()