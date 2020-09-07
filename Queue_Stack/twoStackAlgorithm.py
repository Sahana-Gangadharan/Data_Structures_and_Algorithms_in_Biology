class stack_array:
	def __init__(self):
		self.elements = []

	def length(self):
		return len(self.elements)

	def isEmpty(self):
		return self.length() == 0

	def push(self, value):
		self.elements.append(value)

	def pop(self):
		if self.length()==0:
			print("Error: Stack empty!\n")
			return
		else:
			self.elements.pop()

	def top(self):
		if self.length()==0:
			print("Error: Stack empty!\n")
			return
		else:
			self.elements[-1]

def twoStack(str):
	n=len(str)
	Operand = stack_array()
	Operator = stack_array()
	for i in range(n):
		if str[i].isdigit() == True:
			Operand.push(str[i])
		if str[i] == '+' or str[i] == '-' or str[i] == '*' or str[i] == '/':
			Operator.push(str[i])
		if str[i]==')':
			a = Operator.top()
			Operator.pop()
			print(a)
			b = Operand.top()
			Operand.pop()
			print(b)
			c = Operand.top()
			Operand.pop()
			print(c)
			Operand.push()

	last = Operand.pop()
	print('Answer = %f' %(last))

a = '(3+4)'
twoStack(a)


