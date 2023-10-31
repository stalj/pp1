class C:
    def __init__(self,counter):
        self.counter=counter
    def m1(self):
        return self.counter
    def m2(self):
        self.counter=self.counter+1
    def m3(self):
        self.counter=self.counter-1
    def m4(self,n):
        self.counter=self.counter+n

c=C(5)
print(c.m1())
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
print(c.m1())
