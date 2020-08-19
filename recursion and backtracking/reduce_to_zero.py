num=0
def solve(n):
	global num
	if n==0:
		return
	num+=1
	print(num)
	if n%2==0:
		solve(n//2)
	else:
		solve(n-1)
	return num
print(solve(8))