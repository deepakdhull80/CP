import sys
def pro(arr):
    i=1
    for j in arr:
        i*=j
    return i
dic={}

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,sys.stdin.readline().split()))
    res=0
    def solve(arr,first,last):
        if first==last:
            return
        solve(arr,first,last-1)
        if sum(arr[first:last+1])==pro(arr[first:last+1]) and (first,last) not in dic:
            print(first,last,sum(arr[first:last+1]),pro(arr[first:last+1]))
            res+=1
            print(res)
            dic[(first,last)]=1
        # print(res)
        solve(arr,first+1,last)
        

    solve(arr,0,len(arr)-1)+len(arr)
    print(res)

