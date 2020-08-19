stack=[1,2,3,4]
stack1=[]
def push_bottom(m):
	if len(stack)==0:
		stack.append(m)
		stack.append(stack1[len(stack1)-1])
		stack1.pop()
		return
	stack1.append(stack[len(stack)-1])
	stack.pop()
	push_bottom(m)
	if len(stack1)-1 >=0:
		stack.append(stack1[len(stack1)-1])
		stack1.pop()
push_bottom(0)
print(stack)