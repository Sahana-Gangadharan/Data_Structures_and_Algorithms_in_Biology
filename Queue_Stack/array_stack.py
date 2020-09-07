class stack_array:
	def __init__(self):
		self.elements = []

	def length(self):
		return len(self)

	def isEmpty(self):
		return length(self) == 0

	def push(self, value):
		self.elements.append(value)

	def pop(self):
		if len(self)==0:
			print("Error: Stack empty!\n")
			return
		else:
			self.elements.pop()

	def top(self):
		if len(self)==0:
			print("Error: Stack empty!\n")
			return
		else:
			self.elements[-1]

def stack_Array():
	a = stack_array()
	
	element1 = input("Enter element to initialise the stack - ")
	a.push(element1)

	print("Do you want to continue? Enter Y/N - ")
	decide = str(input())

	while decide == 'Y' or decide == 'y':

		print("Which of the following tasks do you want to do?\n1.Push\n2.Pop\n3.Top\n")
		option = int(input("Enter number : "))
		if option==1:
			element = input("Enter element to push - ")
			a.push(element)
		elif option==2:
			a.pop()
		elif option==3:
			a.top()
		else:
			print("Sorry! Wrong option.\n")
			return
        
		print("Do you want to continue? Enter Y/N - ")
		decide = str(input())

	while decide == 'N' or decide == 'n':

		print("See ya next time!\n")
		return

stack_Array()