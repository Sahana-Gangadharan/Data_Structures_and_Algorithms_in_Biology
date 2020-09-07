def BFS(G,start,finish):
	discovered= []
	queue = [[start]]

	while queue:
		route = queue.pop(0)
		node = route[-1]
		if node not in discovered:
			neighbours = list(G.neighbors(node))
			n = len(neighbours)
			for i in range(n):
				detour = list(path)
				detour.append(neighbours[i])
				queue.append(detour)
				if neighbours[i]==finish:
					return detour
			discovered.append(node)
