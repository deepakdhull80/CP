arr=[1,2,3,4]
n=len(arr)
def subset(arr,ind,cur):
	if len(arr)==ind:
		print(cur)
		return 
	
	subset(arr,ind+1,cur+[arr[ind]])
	subset(arr,ind+1,cur)
subset(arr,0,[])

		

