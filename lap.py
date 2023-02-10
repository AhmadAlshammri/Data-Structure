class queue:
    def __init__(self):
        self.QQu = list()
    def additems(self,dataval):

        if dataval not in self.QQu:
            self.QQu.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.QQu)
    def show(self):
        return self.QQu
    def dlete(self):
        self.QQu.pop(0)
        return True
    def add1(self,value):
         if value not in self.QQu:
            self.QQu.insert(0,value)
            return True
         return False
    def appand(self,val):
        return self.QQu.append(val)
    def pop(self):
        return self.QQu.pop()


Theq = queue()
Theq.additems("mon")
Theq.additems("non")
Theq.additems("n,mk")
Theq.dlete()
Theq.appand("hdgbggc")
Theq.add1("hnf")
Theq.pop()
print(Theq.size())
print(Theq.show())