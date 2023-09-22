class C:

    def __init__(self,x):
        self.x=x
        self.value=x

    def m1(self):
        print(self.value)

    def m2(self):
        self.value+=1

    def m3(self):
        self.value-=1

    def m4(self,n):
        self.value+=n

c=C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1()