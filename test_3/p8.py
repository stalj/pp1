class C():

    def __init__(self,slownik):
        self.slownik=slownik

    def m1(self,s,n):
        self.slownik[s]=n
    
    def m2(self,a):
        sum=0
        for x in a:
            if self.slownik[x]<0:
                pass
            else:
                sum+=self.slownik[x]
        return sum

c=C({"A":120,"D":150,"G":90,"K":110})
c.m1("G",130)
c.m2(["G","D"])
