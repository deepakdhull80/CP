def sqrt(n):
	left=1
	right=n
	while left<=right:
		mid=(left+right)//2
		if mid*mid==n:
			return mid
		if mid*mid>n:
			right=mid-1
		else:
			left=mid+1
print(sqrt(13))