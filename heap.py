class BinHeap:
	
	def __init__(self):
		self.heaplist = [0]
		self.size = 0
	
	def insert(self,data):
		'''
		append data first
		then float it 
		'''
		self.heaplist.append(data)
		self.size += 1
		self.__floating__(self.size)
		
	def pop(self):
		'''
		replace the top node with the last node, and pop top node 
		then sink the new top node
		'''
		if self.isEmpty():
			print('Error: Pop from empty heap')
			return None
		tmp = self.heaplist[1]
		self.heaplist[1] = self.heaplist[-1]
		self.size -= 1
		self.heaplist.pop()
		self.__sinking__(1)
		return tmp
	
	def buildHeap(self,L):
		'''
		sink every father(i < size//2) node
		'''
		self.heaplist = [0] + L
		self.size = len(L)
		i = self.size//2
		while i > 0 :
			self.__sinking__(i)
			i -= 1
		
		
	def show(self):
		print(self.heaplist)
		
	def peak(self):
		return self.heaplist[0]
		
	def isEmpty(self):
		return self.size == 0
	
	def size(self):
		return self.size
	
	def __floating__(self,i):
		while i//2 >0:
			if self.heaplist[i//2] > self.heaplist[i]:
				self.heaplist[i//2],self.heaplist[i] = self.heaplist[i],self.heaplist[i//2]
			i = i//2	
	
	def __sinking__(self,i):
		while i*2 <= self.size:
			if 2*i+1 > self.size:
				m = 2*i
			else:
				if self.heaplist[2*i] > self.heaplist[2*i+1]:
					m = 2*i+1
				else:
					m = 2*i
			if self.heaplist[i] > self.heaplist[m]:
				self.heaplist[i],self.heaplist[m] = self.heaplist[m],self.heaplist[i]
			i = m
						
if __name__ == '__main__':
	bh = BinHeap()
	
	
