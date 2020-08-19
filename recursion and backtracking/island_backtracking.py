ar=[[1,1,1,0],
	[1,0,0,0],
	[1,1,1,0],
	[0,1,1,1]]
n=len(ar)

def solve_check(arr,i,j):
	#base case
	if i==j and j==n-1:
		# print(arr[i][j],i,j)
		return True
	if i==n or j==n:
		# print(arr[i][j],i,j)
		return False
	if arr[i][j]==0:
		# print(arr[i][j],i,j)
		return False
	return (solve_check(arr,i+1,j) or solve_check(arr,i,j+1))
def solve_count_without_store(arr,i,j):
	if i==j and j==n-1:
		# print(arr[i][j],i,j)
		return 1
	if i==n or j==n:
		# print(arr[i][j],i,j)
		return 0
	if arr[i][j]==0:
		# print(arr[i][j],i,j)
		return 0
	return (solve_count_without_store(arr,i+1,j) + solve_count_without_store(arr,i,j+1))
store=[[None]*n]*n
def solve_count_with_store(arr,i,j):
	if i==j and j==n-1:
		return 1
	if i==n or j==n:
		return 0
	if store[i+1][j]!=None:
		x1=store[i+1][j]
	else:
		x1=solve_count_with_store(arr,i+1,j)
	if store[i][j+1]!=1:
		x2=store[i][j+1]
	else:
		x2=solve_count_with_store(arr,i,j+1)
	store[i][j]=x1 or x2
print(solve_check(ar,0,0))
print(solve_count_without_store(ar,0,0))