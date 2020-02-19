#STACK using linked list

class Node:
                def __init__(self,data):
                                self.data=data
                                self.next=None


class Stack:
                def __init__(self,max_length):
                                self.top=None
                                self.max_length=max_length
                                self.elements=0

                def push(self,data):
                                if self.max_length>self.elements:
                                                node=Node(data)
                                                node.next=self.top
                                                self.top=node
                                                
                                                self.elements+=1
                                                self.traverse()
                                                print()
                                else:
                                                print("Lack of space")


                def pop(self):
                                if self.elements==0:
                                                print("Already empty")
                                else:
                                                self.top=self.top.next
                                                self.elements-=1
                                                self.traverse()

                def traverse(self):
                                temp=self.top

                                while temp is not None:
                                                print(temp.data,end="--->")
                                                
