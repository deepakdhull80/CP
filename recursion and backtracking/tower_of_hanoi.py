def hanoi(n,a,b,c):
    global count
    if n==1:
        print(a,' to ',b)
        count+=1
        return
    hanoi(n-1,a,c,b)
    print(a,' to ',b)
    count+=1
    hanoi(n-1,b,c,a)
count=0
print('Enter Number:')
n=int(input())
hanoi(n,'a','b','c')
print(count)