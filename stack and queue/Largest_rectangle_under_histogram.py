#             __
#          __|  |
#         |\\\\\|   _____
#    __   |\\\\\|  |  |  |
#   |  |__|\\\\\|  |  |  |
#   |  |  |\\\\\|__|  |  |
# __|__|__|\\\\\|__|__|__|_____
# 	 3  2   5  6  1  4  4

def left(arr,index):
	if index==0:
		return 0
	i=index-1
	count=0
	while i>=0 and  arr[i]>=arr[index]:
		count+=1
		i-=1
	return count
def right(arr,index):
	if index==len(arr)-1:
		return 0
	i=index+1
	count=0
	while i<=len(arr)-1 and  arr[i]>=arr[index]:
		count+=1
		i+=1
	return count
if __name__=="__main__":
	arr=[3,2,5,6,1,4,4]
	n=len(arr)
	res=0
	for i in range(n):
		base=1
		l=left(arr,i)
		r=right(arr,i)
		res=max((l+r+base)*arr[i],res)
	print(res)