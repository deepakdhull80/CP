arr=[-3,-1,0,4,6,8,9]
val=-2
l=0
r=len(arr)-1
f=0
while l<=r:
	mid =(l+r)//2
	if arr[mid]==val:
		print(val)
		f=1
		break
	if arr[mid]<val:
		# print(arr[mid])
		if mid+1 <=r and arr[mid+1]>val:
			qw=abs(arr[mid+1]-val)
			wq=abs(arr[mid]-val)
			if qw<=wq:
				f=1
				print(arr[mid+1])
				break
				# f=1
			else:
				print(arr[mid])
				f=1
				break
				# f=1
		else:
			l=mid+1
	else:
		if arr[mid-1]<val:
			qw=abs(arr[mid-1]-val)
			wq=abs(arr[mid]-val)
			if qw<=wq:
				f=1
				print(arr[mid-1])
				# break

			else:
				f=1
				print(arr[mid])
				# break
		else:
			r=mid-1

if f==0:
	if l==0:
		print(arr[l])
	else:
		print(arr[r])