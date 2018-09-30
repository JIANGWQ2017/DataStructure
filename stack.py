class Stack:
	'''
	last in first out
	'''
	def __init__(self):
		#private attribute
		self.__items = []
		
	def push(self,item):
		self.__items.append(item)
		
	def pop(self):
		try:
			return self.__items.pop()
		except:
			return None
		
	def isEmpty(self):
		return not bool(len(self.__items))
		
	def size(self):
		return len(self.__items)
	