
def preOrderTrav(root):
	'''
	preorder traversal
	'''
	if root is not None:
		print(root.data)
		preOrderTrav(root.left)
		preOrderTrav(root.right)

def inOrderTrav(root):
	'''
	inorder traversal
	'''
	if root is not None:
		inOrderTrav(root.left)
		print(root.data)
		inOrderTrav(root.right)

def postOrderTrav(root):
	'''
	postorder traversal
	'''
	if root is not None:
		postOrderTrav(root.left)
		postOrderTrav(root.right)
		print(root.data)

#using queue to realize BFTrav		
from queue import Queue
def BFTrav(root):
	q = Queue()
	q.enqueue(root)
	while not q.isEmpty():
		node = q.dequeue()
		print(node.data)
		if node.left:
			q.enqueue(node.left)
		if node.right:
			q.enqueue(node.right)
		
		
		
class BinTreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		
class BinaryTree:
	'''
	binary search tree
	'''
	def __init__(self):
		self.root = None 
		
	def addNode(self,nodeordata):
		if isinstance(nodeordata,BinTreeNode):
			item = nodeordata
		else:
			item = BinTreeNode(nodeordata)
		
		if not self.root:
			self.root = item
		else: 
			node = self.root
			while True:
				if item.data == node.data:
					print('Error: The value you input has already existed in the tree')
				elif item.data > node.data:
					if node.right == None:
						node.right = item
						break
					else:
						node = node.right
				else: 
					if node.left == None:
						node.left = item
						break
					else:
						node = node.left
	
	def isEmpty(self):
		return not self.root
	
	def search(self,val):
		if self.isEmpty():
			return False
		else:
			node = self.root
			while node:
				if val == node.data:
					return True
				elif val > node.data:
					node = node.right
				else:
					node = node.left
			return False
	
	def deleteNode(self,val):
		if self.isEmpty():
			print('Error: The tree is empty')
			return None
		p = self.__findTargetParent__(val)
		if not p:
			print('Error: Node not in tree')
			return None
		# node exists in tree	
		flag = None 
		if p.right == None:
			node = p.left
			flag = 'left'
		elif p.left == None:
			node = p.right 
			flag = 'right'
		else:
			if p.right.data == val:
				node = p.right
				flag = 'right'
			else:
				node = p.left
				flag = 'right'
		if node.right and node.left:
			min = self.__minNode__(node.right)
			node.data = min.data
			self.deleteNode(min.data)
			
		elif node.right and not node.left:
			if flag =='right':
				p.right = node.right
			else:
				p.left = node.right
		elif node.left and not node.right:
			if flag =='right':
				p.right = node.left
			else:
				p.left = node.left
		else:
			if flag == 'right':
				p.right = None
			else:
				p.left = None
				
				
	def __findTargetParent__(self,val):
		if self.isEmpty():
			return None
		else:
			node = self.root
			if node.data == val:
				return node
			else:
				while node:
					if node.right.data == val or node.left.data == val:
						return node
					elif val > node.data:
						node = node.right
					else :
						node = node.left
				return None
	
	def __minNode__(self,root):
		node = root
		while node.left:
			node = node.left
		print(node.data)
		return node
	
if __name__ == '__main__':
	bst = BinaryTree()
	for i in range(5):
		bst.addNode(i)
	for i in range(-5,0):
		bst.addNode(i)
	preOrderTrav(bst.root)
	print()
	inOrderTrav(bst.root)
	print()
	postOrderTrav(bst.root)
	print()
	BFTrav(bst.root)
	print(bst.search(4))
	print()
	bst.deleteNode(-4)
	BFTrav(bst.root)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
