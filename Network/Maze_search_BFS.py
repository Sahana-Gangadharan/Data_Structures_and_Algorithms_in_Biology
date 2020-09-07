#Name - Sahana
#Roll Number - BE17B038
#Collaborators - BE17B026
#Time - 30:00 mins

def RegularLattice(n, k):

	import networkx as nx
	ctr=0
	H = nx.Graph()
	nodes = list(range(n)) #n = number of nodes in that sequential order.
	H.add_nodes_from(nodes) #Graph H has n nodes now.
	join = []
	for j in range(n):
		for i in range(1,k+1): 
			p = j+i #k times on right direction,
			q = j-i #k times on left direction,
			if p>=n:
				p=p-n
			join.append(nodes[p]) #Nodes that need to be joined to the given node are appended to this list
			join.append(nodes[q])
			#print(join)
		for l in range(2*k):
			H.add_edge(j,join[l]) #Edges are formed by joining nodes.
		join=[]

	#verification - Each node should have 2*k neighbours. If not, it prints an error and exits the function.
	for i in range(n):
		neighbours = len(list(H.neighbors(j)))
		if neighbours!=(2*k):
			print('Error')
			exit()
		else:
			ctr+=1
	print('Number of nodes with neighbours = 2*k (6 in our case) is expected to be n (all the nodes). And it is observed to be %d (equal to n). Hence, verified!' %ctr)
	nx.draw(H)
	return H

if __name__ == '__main__':
	RegularLattice(50,3)