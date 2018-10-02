class HashTable:
	def __init__(self,size):
		self.size = size
		self.hashtable = [None for i in range(size)]
		self.p = size
		
	def hash(self,key):
		'''
		hash function: mod method
		p value is the maximun of hashtable
		'''
		return key % self.p 
	
	def insert(self,key):
		address = self.hash(key)
		while self.__conflict__(address):
			address = (address+1) % self.p
		self.hashtable[address] = key
	
	def search(self,key):
		address = self.hash(key)
		ad = address
		while self.hashtable[address] != key:
			address = (address+1) % self.p
			if not self.hashtable[address] or address == ad:
				return False
		return True
	
	def __conflict__(self,address):
		return self.hashtable[address]
		
		
if __name__ == '__main__':
	a = [12,54,23,67,32,18,83,63,40,89,99,39]
	hashtable = HashTable(12)
	for i in a:
		hashtable.insert(i)
	print(hashtable.search(23))
	print(hashtable.search(100))