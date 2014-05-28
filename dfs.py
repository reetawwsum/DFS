#Depth First Search with topological sort
g = {}
explored = {} #0: Unexplored, 1: Explored
finishingTime = {}

def dfs(g, s):
	global label
	explored[s] = 1
	for v in g[s]:
		if not explored[v]:
			#print v,
			dfs(g, v)
	finishingTime[s] = label
	label -= 1

def topologicalSort(g):
	for v in g:
		if not explored[v]:
			dfs(g, v)

with open('input.txt', 'r') as graphInput:
	for line in graphInput:
		ints = [int(x) for x in line.split()]
		g[ints[0]] = ints[1:]
		explored[ints[0]] = 0

label = len(g) #For defining finishing time in topological sort

#dfs(g, 1)
topologicalSort(g)