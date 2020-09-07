# BT3051 Assignment 1b
# Roll Number - BE17B038
# Time - 7:00:00
# Identify Open Reading Frames, Translate mRNA to Protein, Calculate Protein Mass
import sys
import doctest

def read_FASTA(filename):
    """
    (str)->(list of tuples)
    Reads a fasta file. Differentiates sequence name and sequence. Returns a list of tuples of (seqname,seq)
    """
    fasta=[]
    with open(filename,'r') as f:
        seq=''
        # Reads line by line
        line=f.readline()
        # Removes '\n' and similar strings
        line=line.strip()
        if line[0]=='>':
            #Sequence name is always preceeded by a '>'
            seq_name=line[1:]
        # From the next line, until it meets another '>', it is added to the sequence 
        line=f.readline()
        line=line.strip()
        seq+=line
        
        for line in f:
            line=line.strip()
            if line[0]=='>':
                #Sequence name is always preceeded by a '>' Existing seqname and seq are appended
                fasta.append((seq_name,seq))
                seq=''
                seq_name= line[1:]
                continue
            seq+=line
            
        fasta.append((seq_name,seq))
        
    return fasta

def identify_orfs(dnaStrand):
    """ (str) -> (list of strings) 
    # Identifies Open reading frame which begins and ends with start and stop codon respectively. 
    >>>identify_orfs("ATGAAATAGCCC")
    ATGAAATAG
    """
    n=len(dnaStrand)
    # COMPLEMENT is a dictionary with the Keys and Values denoting the complementary base pairing of DNA
    def compliment(string):
        COMPLEMENT = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        # each character from strin (dna) is complemented. the entire string is reversed and jooined without leaving any space.
        rstring=''.join(reversed([COMPLEMENT[base] for base in string]))
        return rstring
    frames=[]
    seq=''
    
    for i in range(n-3): 
        # Small is a set of 3 consecutive nucleotides
        small=dnaStrand[i:i+3]
        # If small is the startcodon
        if small=='ATG':
            for j in range(i,n-3,3):
                #seq stores the set of nucletides (reading frame) until a stop codon is read
                seq+=small
                small=dnaStrand[j:j+3]
            # once a stop codon is encountered, the sequence (reading frame) is appended to a list
            frames.append(seq)
            # seq is reassigned to ''
            seq=''
    print(frames)
    return frames

def translate_DNA(dnaStrand):
    """ 
    (str)->(str)
    # Based on the dictioary - Codon which is equivalent to the Codon table, the dnaStrand is converted to rnaStrand first and then translated
    >>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
    MYDATASTRCTRES
    """
    protein =''
    # rnaStrand is dnaStrand with U in place of T
    rnaStrand = dnaStrand.replace('T','U')
    n = len(rnaStrand)
    # Codon Table as a dictionary
    Codon = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L', 'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', 'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M','GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V','UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S','AGU' : 'S', 'AGC' : 'S', 'CCA' : 'P', 'CCG' : 'P','CCU' : 'P', 'CCC' : 'P', 'ACA' : 'T', 'ACG' : 'T','ACU' : 'T', 'ACC' : 'T', 'GCA' : 'A', 'GCG' : 'A','GCU' : 'A', 'GCC' : 'A', 'UAU' : 'Y', 'UAC' : 'Y','CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q','AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K','GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E','UGU' : 'C', 'UGC' : 'C', 'UGG' : 'W', 'AGA' : 'R','CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R','AGG' : 'R', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G','GGU' : 'G', 'UAA' : '' , 'UAG' : '', 'UGA' : ''}
    for i in range(0,n-1,3):
        # rnaStrand is translated
        small=rnaStrand[i:i+3]

        protein+=Codon[small]

    return protein

def compute_protein_mass(protein_string):
    """ 
    (str)->(float)
    #The translated protein is traversed, and the total mass of the polypeptide sequence is computed based on the PROT_MASS dictionary which specifies mass of each aminoacid.
    >>> compute_protein_mass('SKADYEK') 
    821.392 
    """
    list_seq = list(protein_string)
    n = len(list_seq)
    print(n)
    mass=0
    # Dictonary referring to each AA's mass
    PROT_MASS = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496, 'L' : 113.08406, 'M':131.04049, 'N':114.04293, 'P': 97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 'T':101.04768, 'U':0,'V' : 99.06841, 'W':186.07931, 'Y':163.06333}
    for i in range(n):
        chars = list_seq[i]
        mass+= PROT_MASS[chars]

    return mass

if __name__ == '__main__': 
	#DO NOT CHANGE THE FOLLOWING STATEMENTS 
	for seq_name , seq in read_FASTA("G:/Textbook-Sem5/BT3051 Data Structures and Algorithms/Assignments/hw1b_dataset.faa"): 
		print (seq_name+':')
		for orf in identify_orfs(seq):
			protein=translate_DNA(orf)
			print(protein,compute_protein_mass(protein))