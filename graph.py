import sys

class graph:
	def __init__(self,nodeNum,adjacentMatrix):
		self.nodeNum = nodeNum
		self.adjacentMatrix = adjacentMatrix
		

	def traverse(self,algorithm):
		# 由于有些点是孤立点， 所以需要对每个节点进行_dfs， 用visited 来避免重复访问
		visited = [0 for i in range(self.nodeNum)]
		
		if algorithm.lower() == 'bfs':
			order = []
			for i in range(self.nodeNum):
				if visited[i] == 0:
					order.extend(self._bfs(i,visited))
			
			print(order)
		if algorithm.lower() == 'dfs':
			order = []
			for i in range(self.nodeNum):
				if visited[i] == 0:
					order.extend(self._dfs(i,visited))
			
			print(order)

	def _bfs(self,node,visited):
		
		# 遍历过的节点按顺序放在order list中
		order = []
		# 入过栈的节点
		inqueue = [0 for i in range(self.nodeNum)]
		# 待访问的节点
		stack = [node]
		inqueue[node] = 1
		
		while stack:
			cur  = stack.pop(0)
			order.append(cur)
			visited[cur] = 1
			for i in range(len(self.adjacentMatrix[cur])):
				if self.adjacentMatrix[cur][i] == 1 and inqueue[i] == 0:
					stack.append(i)
					inqueue[i]=1
		return order

	
	def _dfs(self, node, visited):
		# 已经入过栈的节点，而不是已经访问过的节点
		inqueue = [0 for i in range(self.nodeNum)]
		# 待访问的节点
		stack = [node]
		#保存dfs遍历顺序		
		order = []
		
		inqueue[node] = 1
		while stack:
			cur = stack.pop()
			visited[cur] = 1
			order.append(cur)
			for i in range(len(self.adjacentMatrix[cur])):
				if self.adjacentMatrix[cur][i]==1 and inqueue[i] == 0:
					stack.append(i)
					inqueue[i] = 1
		return order

class edgeParser:
	
	def __init__(self):
		self.edges  = []
		
		
	def parsing(self,line):
		line = line.strip().split(' ')
		line = [s for s in line if s]
		if len(line)==2:
			self.edges.append(line)
		
		
	def generateAdjacentMatrix(self,nodeNum):
		adjacentMatrix = [[0 for j in range(nodeNum)] for i in range(nodeNum)]
		for edge in self.edges:
			edge[0],edge[1] = int(edge[0]),int(edge[1])
			adjacentMatrix[edge[0]][edge[1]] = 1
			adjacentMatrix[edge[1]][edge[0]] = 1
		return adjacentMatrix
		
		

def main():
	nodes_num = None
	# 节点序号从0  ->  n-1
	while not nodes_num:
		nodes_num = input('Please input number of vertices(required > 0): ')
	ep = edgeParser()
	while True:
		line = sys.stdin.readline()
		if line.rstrip().strip() == '':
			break
		else:
			ep.parsing(line)
	nodes_num = int(nodes_num)
	adjacentMatrix = ep.generateAdjacentMatrix(nodes_num)
	
	G = graph(nodes_num, adjacentMatrix)
	#G.traverse('bfs')
	G.traverse('dfs')	
	
if __name__ == "__main__":
	main()