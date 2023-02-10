class Node:
    def __init__(self,datava1=None):
        self.datava1=datava1
        self.nextval=None
class sl:
    def __init__(self):
        self.headval =None
    def listp(self):
        prival=self.headval
        while prival is not None:
            print(prival.datava1)
            prival=prival.nextval
    def atbiagning(self,newdata):
       newnode= Node(newdata)
       newnode.nextval=self.headva1
#       self.headva1=newnode
list = sl()
list.headval=Node("mon")
e2 =Node("tue")
e3=Node('wed')
list.headval.nextval=e2
e2.nextval=e3
list.atbiagning("sun")
list.listp()

        