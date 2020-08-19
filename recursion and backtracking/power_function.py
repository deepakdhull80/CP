#complexity is O(log(n))
def po(a,n):
	if n==1:
		return a
	# print(power(a,n//2))
	x=po(a,n//2)

	if n %2== 1:
		return(x*x*a)
	else:
		return(x*x)

def using_without_recursion(a,n):
	res=1
	while(n>0):
		if n%2==1:
			res*=a
		n=n>>1
		a=a*a
	return res
def for_negative(a:float,n:int)-> float:
	if n==0:
		return 1
	if n<0:
		n=-n
		a=1/a
	def help(a,n):
		if n==1:
			return a
		ans=help(a,n//2)
		if n%2==0:
			return ans*ans
		else:
			return ans*ans*a
	return help(a,n)
print(po(3,10))
print(po(2,3))
print(using_without_recursion(3,10))
print(round(for_negative(2,-10),6))