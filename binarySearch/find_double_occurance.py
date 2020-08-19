a1=[1,2,3,4,5,6,7,7]
a2=[1,1,2,3,4,5,6,7]
a3=[1,2,3,4,4,5,6,7]

def find(arr):
	l,r=0,len(arr)-1
	while l<r:
		mid =(l+r)//2
		if arr[mid] != mid:
			l=mid+1
		else:
			r=mid-1
	return arr[l]
print(find(a1))
print(find(a2))
print(find(a3))