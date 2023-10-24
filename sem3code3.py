#Formation of linked list and adding in the beginning.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def addbeg(self):
        d=int(input("Enter the data value"))
        temp=node(d)
        if (self.head==None):
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp


    
    
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next


l=linkedlist()
l.addbeg()
l.addbeg()
l.display()
