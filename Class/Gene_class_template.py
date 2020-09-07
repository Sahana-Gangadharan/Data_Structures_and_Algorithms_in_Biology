# BT3051 Assignment 1a
# Roll Number - BE17B038
# Time - 1:30:00

class Gene:
	ctr = 0 # ctr is a variable that will be later used to calculate the GC content.
	# Initialising a Gene Class with gene ID and the sequence. Both these are given as arguments
	def __init__(self,ID,string):
		self.geneID = str(ID)
		self.sequence = str(string)
	# len() method to return the length of the sequence.
	def __len__(self):
		return len(self.sequence)
	# repr() method specifying the representation of any instance from the Gene class.
	def repr(self):
		return str(self.geneID) + ' : ' + str(self.sequence)
	# function to compute GC content in the sequence
	def GC_content(self):
		n=len(self.sequence)
		string = self.sequence
		ctr = 0
		# In the for loop, we traverse through the string and count the number (stored in ctr) of occurances of G and C
		for i in range(n):
			if string[i]=='G' or string[i]=='C':
				ctr+=1
		# The percentage of gc content is ctr/(string length)*100
		gc_content = (ctr/n)*100
		print('GC Content in the DNA = %f' %gc_content)
		return 
	# Addition of two instances of the gene class will add the sequences of both the genes. Output will also be an instance of the class.
	def __add__(self,other):
		result = Gene('','')
		result.sequence = self.sequence + other.sequence
		return result
	# Subtraction of two instances of the gene class will subtrance the sequence of latter from former gene. Output will also be an instance of the class.
	def __sub__(self,other):
		result = Gene('','')
		result.sequence = self.sequence - other.sequence
		return result
	# The string reprentation of the gene's sequence
	def __str__(self):
		return '"' + str(self.sequence) + '"'
	# Compliment function is used to find the reversed complementary stand of the Gene's sequence
	def compliment(string):
		# COMPLEMENT is a dictionary with the Keys and Values denoting the complementary base pairing of DNA
		COMPLEMENT = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
		# each character from strin (dna) is complemented. the entire string is reversed and jooined without leaving any space.
		result = Gene('','')
		rstring=''.join(reversed([COMPLEMENT[base] for base in string]))
		result.sequence = rstring
		print(rstring)
		return result

a=Gene("DNA1","AGCTGCATGTACGTAGTCA")
b=Gene("DNA2","TCATCGGTAGCAATTT")
a.GC_content()
a=a+b
complement(a.sequence)
print(type(c))
c.sequence

