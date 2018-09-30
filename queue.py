class Queue:
	'''
	first in first out
	'''
	def __init__(self):
		self.items = []
	
	def size(self):
		return len(self.items)
		
	def isEmpty(self):
		return self.items == []
	
	def enqueue(self,item):
		self.items.append(item)
	
	def dequeue(self):
		try:
			return self.items.pop(0)
		except: 
			return None
	