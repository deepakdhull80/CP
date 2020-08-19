#Find the single occurance element in sorted array
ar=[2,2,3,1,1,5,5]

def find_single_occurance(arr):
	left=0
	right=len(arr)-1
	if right==0:
		return arr[right]
	while left<=right:
		mid =(left+right)//2
		print(mid)
		if mid == len(arr)-1 or mid == 0:
			return arr[mid]

		if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
			return arr[mid]
		if arr[mid]==arr[mid-1]:
			left=mid+1
		else:
			right=mid-1

print(find_single_occurance(ar))