arr=[[2,3],[9,18],[2,5],[3,7],[15,20]]
arr.sort()
# print(arr)
# [[2, 3], [2, 5], [3, 7], [9, 18], [15, 20]] 
n=len(arr)
i=0
j=1
res=[arr[0]]
# print(arr)
# print(res)
while j<n:
    if arr[j-1][1]>=arr[j][0]:
        res[-1][1]=arr[j][1]
        j+=1
    else:
        res.append(arr[j])
        i=j
        j=j+1
    # print(res)
print(res)