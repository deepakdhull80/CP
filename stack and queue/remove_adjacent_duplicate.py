data=list('carrreerrrrmonk')
print(data)
from collections import deque
stack=deque()
queue=deque()
for i in data:
	if len(stack)==0:
		stack.append(i)
	else:
		if stack[-1]==i:
			queue.append(stack.pop())
		elif len(queue) and i==queue[0]:
			queue.popleft()
		else:
			stack.append(i)
print(stack)