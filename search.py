# sequential search  
# time complexity O(n)
def sequential_search(L, key):
	'''
	L: input list
	key: the value you look for 
	If searched, return index else return False
	'''
	for i in range(len(L)):
		if L[i] == key:
			return i
	return False

# ordered search
#1. binary search 
def binary_search(orderedlist, key):
	low = 0
	high = len(orderedlist)-1

	while low <= high:
		mid = (low+high)//2
		if key == orderedlist[mid]:
			return mid
		elif key < orderedlist[mid]:
			high = mid-1
		else:
			low = mid+1
	return False

#2. modified binary search
def modified_binary_search(orderedlist, key):
	low = 0
	high = len(orderedlist)-1
	while low < high:
		mid = low + int((high-low)*(key-orderedlist[low])/(orderedlist[high]-orderedlist[low]))
		if key == orderedlist[mid]:
			return mid
		elif key < orderedlist[mid]:
			high = mid-1
		else:
			low = mid+1
	return False

	
if __name__ == '__main__':
	a = [1,2,3,4]
	for i in range(5):
		print(binary_search(a,i))
	for i in range(5):
		print(modified_binary_search(a,i))