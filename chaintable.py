class node:
	def __init__(self,data,next = None):
		self.data = data
		self.next = next
		
	def __repr__(self):
		return self.data

		
class ChainTable:
	'''
	index starts from 0
	'''
	def __init__(self):
		self.length = 0
		self.head = None
		
	def isEmpty(self):
		return self.length == 0
	
	def append(self, dataornode):
		if isinstance(dataornode,node):
			item = dataornode
		else:
			item = node(dataornode)
		
		if self.head == None:
			self.head = item
			self.length += 1 
		else:
			n = self.head
			while n.next:
				n = n.next
			n.next = item
			self.length += 1
			
	def insert(self,index,dataornode):
		if self.isEmpty():
			print('Error: chaintable is empty')
			return None
			
		elif self.length <= index or index < 0:
			print('Error: Out of index')
			return None
		
		if isinstance(dataornode,node):
			item = dataornode
		else:
			item = node(dataornode)
		
		if index == 0:
			item.next = self.head
			self.head = item
			self.length += 1
		else:
			n = self.head
			for i in range(index-1):
				n = n.next
			item.next = n.next
			n.next = item
			self.length += 1
			
	def length(self):
		return self.length
	
	def delete(self,index):
		if self.isEmpty():
			print('Error: chaintable is empty')
			return None
			
		elif self.length <= index or index < 0:
			print('Error: Out of index')
			return None
		
		if index == 0:
			self.head = self.head.next
			self.length -= 1
		else:
			n = self.head
			for i in range(index-1):
				n = n.next
			n.next = n.next.next
			self.length -= 1
			
	def show(self):
		if not self.head:
			print('Empty chaintable')
		else:
			val = []
			n = self.head
			while n.next:
				val.append(n.data)
				val.append(' -> ')
				n = n.next
			val.append(n.data)
			for v in val:
				print(v,end = '')
			print('')
			
	def clear(self):
		self.head = None
		self.length = 0
		
	def update(self,index,data):
		if self.isEmpty() or index < 0 or index > self.length:
			print('Error: Out of Index')
		else: 
			n = self.head
			for i in range(index):
				n = n.next
			n.data = data
	
	def getItem(self,index):
		if self.isEmpty() or index < 0 or index > self.length:
			print('Error: Out of Index')
		else:
			n = self.head
			for i in range(index):
				n = n.next
			return n.data
	
if __name__ == '__main__':
	ct = ChainTable() 
	for i in range(10):
		ct.append(i)
	print("初始链表")
	ct.show()
	ct.insert(5,11)
	print("index为5的位置插入11")
	ct.show()
	ct.delete(2)
	print("删除index为2的节点")
	ct.show()
	print("更新index为7的节点值为12")
	ct.update(7,12)
	ct.show()
	print("获得index为3的节点值")
	print(ct.getItem(3))