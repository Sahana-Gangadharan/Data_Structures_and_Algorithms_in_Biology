#Name - Sahana
#Roll number - BE17B038
#Collaborators - BS17B033
#Time - 2:30 hours

def maze(MazeMatrix,start,finish):
    #MazeMatrix is a binary matrix (2D list of lists)
    #start & finish are tuples containing the starting and finishing point indices e.g. (1,1) & (5,5)
    
    import networkx as nx
    
    def MazeMatrix2Graph(MazeMatrix):
        #MazeMatrix is a binary matrix (2D list of lists)
        
        MazeGraph = nx.Graph()
        m = len(MazeMatrix) #Number of rows in the matrix
        n = len(MazeMatrix[1]) #Number of columns in the matrix
        for i in range(m):
            for j in range(n):
                if MazeMatrix[i][j]==1:
                    MazeGraph.add_node((i,j)) #Labelling of node as a tuple

        #Connecting the paths from matrix as an edge
        for i in range(m-1): 
            for j in range(n-1):
                if MazeMatrix[i][j]==1:
                    if MazeMatrix[i+1][j]==1:
                        MazeGraph.add_edge((i,j),(i+1,j))
                    if MazeMatrix[i][j+1]==1:
                        MazeGraph.add_edge((i,j),(i,j+1))

        for j in range(n-1):
            if MazeMatrix[m-1][j]==1:
                if MazeMatrix[m-1][j+1]==1:
                    MazeGraph.add_edge((m-1,j),(m-1,j+1))
                
        for i in range(m-1):
            if MazeMatrix[i][n-1]==1:
                if MazeMatrix[i+1][n-1]==1:
                    MazeGraph.add_edge((i,n-1),(i+1,n-1))
                
        # nx.draw(G,with_labels=True) #Representation of graph. But not a necessary output

        return MazeGraph #A networkx graph whose nodes represent the '1's in the input matrix. node labels are tuples.
    
    def MazeAnswerBFS(MazeGraph,start,finish):
        #MazeGraph is a networkx graph 
        #start and finish are tuples containing the starting and finishing point indices
        discovered=[]
        queue=[[start]]
        while queue: #While queue is not zero, meaning that we are still visiting nodes.
            route = queue.pop(0) #Popping the first element makes it FIFO - Hence a queue.
            node = route[-1]
            if node not in discovered:
                neighbours = list(MazeGraph.neighbors(node))
                n = len(neighbours)
                for i in range(n): #When there are multiple neighbours, consider each case one by one in a forloop
                    detour = list(route)
                    detour.append(neighbours[i])
                    queue.append(detour)
                    if neighbours[i]==finish: #If the chosen neighbour to the node is indeed the finish tuple,
                        return detour #Detour will be our shortest path in this case. Hence, we return it.
                discovered.append(node) 
    
    def MazeComponentsDFS(MazeGraph):
        #MazeGraph is a networkx graph
        
        visited = [] #Stores all the visited nodes in the graph
        allnodes = list(MazeGraph.nodes())
        length = len(allnodes)
        components = [] #Final answer - Components of the Graph.
        dfs = [] #Pre final answer. Stores the connected components for each new component/node.
    
        def connected_comp(MazeGraph,node):
            visited.append(node) #All visited nodes are appended to this list
            dfs.append(node) #Connected nodes in this component are appended here
            neighbours = list(MazeGraph.neighbors(node))
            n = len(neighbours)
            for i in range(n):
                if neighbours[i] not in visited:
                    connected_comp(MazeGraph,neighbours[i]) #Recursively call the function to check all the connected nodes in a component
            return dfs #Connected nodes in that component

        for i in range(length):
            if allnodes[i] in visited: #If the node is already visited, then it does not belong to a new component. So, exit from the loop.
                exit()
            else:
                components.append(connected_comp(MazeGraph,allnodes[i])) #Append all the components.
                dfs=[] #Empty this list so that a new component can be added afreash.
        return components #list of lists, each containing tuples of the indices of points in that component
    
    #Function calling to print output
    MazeGraph = MazeMatrix2Graph(MazeMatrix) 
    a = MazeAnswerBFS(MazeGraph,start,finish)
    b = MazeComponentsDFS(MazeGraph)
    print(a)
    print('\n')
    print(b)
    
    #a is the output of MazeAnswerBFS and b is the output of MazeComponentsDFS

if __name__ == '__main__':
    #DO NOT MODIFY THE FOLLOWING
    hw3bmaze=    [[1,0,1,1,0,1],
                  [1,1,0,0,0,0],
                  [0,1,0,1,1,1],
                  [0,1,1,1,0,1],
                  [1,0,0,1,1,1],
                  [1,1,0,0,0,1],
                  [0,0,1,1,0,1]]
    
    hw3bstart=(0,0)
    hw3bfinish=(6,5)
    print(maze(hw3bmaze,hw3bstart,hw3bfinish))
    
#output for this example should be:
#[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5)]
#[[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (3, 5), (2, 5), (2, 4), (2, 3)], [(0, 2), (0, 3)], [(0, 5)], [(4, 0), (5, 0), (5, 1)], [(6, 2), (6, 3)]]
