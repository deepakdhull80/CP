class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linklist:

    def __init__(self):
        self.head=None
        self.last=None

    def push(self,data):
        tmp=self.head
        if tmp==None:
            tmpi=node(data)
            print(tmpi.data)
            tmp=tmpi
        else:
            
            while(tmp.next is not None):
                tmp=tmp.next
            n=node(data)
            tmp.next=n
    def print_link(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next
    def reverse(self):
        prev = None
        current=self.head
        while(current is not None): 
            next=current.next
            current.next=prev 
            prev=current 
            current=next
        self.head=prev
    def length(self):
        cur=self.head
        l=0
        while cur is not None:
            l+=1
            cur=cur.next
        return l 
    def ispalindrome(self):
        first=self.head
        fast=first            

no=linklist()
no.push(2)
no.push(4)
no.push(5)
no.print_link()
no.reverse()
no.print_link()
print(no.length())