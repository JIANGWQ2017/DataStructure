def  solution(m,n,k):
	
	result = []
	backtrack(m,n,1,k,result)
	return len(result)
	
	
	
	
	
def backtrack(M,N,count,k,result):
	if count > k:
		if not M and not N:
			result.append(1)
		return 
	if M:
		for i in range(M+1):
			backtrack(M-i,N,count+1,k,result)
	if N:
		for i in range(N+1):
			backtrack(M,N-i,count+1,k,result)
	
	
def main(m,n,k):
	print(solution(m,n,k))
	
if __name__ == "__main__":
	main(2,2,3)