# triple subarray sum in  array
dic={}
def solve(arr,m):
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i!=j:
				if arr[i]+arr[j] not in dic:
					dic[arr[i]+arr[j]]=[i,j]
				else:
					dic[arr[i]+arr[j]].append([i,j])
	c=0
	for i in range(len(arr)):
		if m-arr[i] in dic and i not in dic[m-arr[i]]:
			print(i,dic[m-arr[i]])
			c+=1
	return c
arr=[1,0,3,4,5]
m=5
print(solve(arr,m))
print(dic)