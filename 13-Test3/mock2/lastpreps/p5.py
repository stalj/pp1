class C:
    def __init__(self,t):
        self.t=t
    def __str__(self):
        sum=0
        a=''
        for i,num in enumerate(self.t):
            sum=sum+num
            a=a+str(num)
            if i<len(self.t)-1:
                a=a+"+"
        a=a+"="
        a=a+str(sum)

        return a



print(C([5,12]))
#print(C([6,0,15]))
