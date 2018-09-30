class Deque:
	'''
	add element or pop element at both ends
	'''
	
	def __init__(self):
		self.items = []
	
	def size(self):
		return len(self.items)
	
	def isEmpty(self):
		return self.items == []
	
	def addFront(self,item):
		self.items.insert(0,items)
	
	def popFront(self):
		try:
			return self.items.pop(0)
		except:
			return None 
	
	def addRear(self,item):
		self.items.append(item)
	
	def popRear(self):
		try:
			return self.items.pop()
		except:
			return None