arr=[0,0,0,0]
dic={}
def count(arr):
	res=0
	s=0
	if len(arr)<=1:
		if arr[0]==0:
			return 1
		else:
			return 0
	for i in range(len(arr)):
		s+=arr[i]
		if s == 0:
			res+=1
		if s not in dic:
			dic[s]=[i]
		else:
			res+=len(dic[s])
			dic[s].append(i)
	return res

print(count(arr))