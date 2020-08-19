#total number of stairs - here we can use dp as well as recursion
def jump(n):
	if n<=1:
		return n
	return jump(n-1)+jump(n-2)
	# print(ans)
	return ans
def jump_dp(n):
	dp=[]
	dp.append(0)
	dp.append(1)
	n-=1
	while(n):
		dp.append(dp[-1]+dp[-2])
		n-=1
	return dp[-1]
print('By recursion %d'%(jump(7)))

print('By Dp %d'%(jump_dp(7)))
