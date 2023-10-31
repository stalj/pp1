class C:
    def __init__(self,t):
        self.t=t
    def m(self):
        for i in range(0,len(self.t)):
            if i%2==0:
                if self.t[i]%2!=0:
                    return False
            else:
                if self.t[i]%2==0:
                    return False
        return True
print(C([8,5,6,7,8,1,2]).m())
print(C([6,3,6,2,4]).m())