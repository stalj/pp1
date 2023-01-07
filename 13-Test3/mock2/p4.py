class C:
    def __init__(self,t):
        self.t=t
    def m(self):
        a=[]
        for i in range(1,len(self.t)):
            a.append(self.t[i]-self.t[i-1])
        print(a)
        if all(x==a[0] for x in a):
            return a[0]
        else:
            return -1
            

print(C([7,10,13,16]).m())
print(C([5,10,15,25,30,351]).m())
print(C([5,10,15,20]).m())