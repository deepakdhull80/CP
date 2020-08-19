
class node:
	def __init__(self,data):
		self.data=data
		self.next=None

	def push(self,data):
		tmp=node(data)
		head=self
		while(head.next is not None):
			head=head.next
		head.next=tmp
	def print_list(self):
		head=self
		while(head is not None):
			print(head.data,end='->')
			head=head.next
		print('Null')

	def delete_node(self,data):
		start=self
		head=self.next
		pre=self
		if (pre.data==data):
			pre.next=None
			return head
		else:
			while head is not None:
				if head.data==data:
					pre.next=head.next
					break
				pre=head
				head=head.next
			return start 
	def reverse(self):
		current=self
		nex=current.next
		pre=None
		while(current is not None):
			current.next=pre
			pre=current
			current=nex
			if nex is not None:
				nex=nex.next
		return pre
	res=None
    def reverse_using_recursion(self,pre,nex):
        global res
        if nex==None:
            self.res=pre
            print(self.res.data)
            return 
        # print(nex.data)
        self.reverse_using_recursion(nex,nex.next)
        # print(nex.data)
        nex.next=pre
		

head=node(1)
head.push(45)
head.push(34)
head.push(12)
head.print_list()
head=head.delete_node(1)
head.print_list()
head=head.delete_node(12)
head.print_list()
head.push(12)
head.push(44)
head.push(199)
head.print_list()
head=head.reverse()
head.print_list()
head.reverse_using_recursion(None,head)
head.res.print_list()