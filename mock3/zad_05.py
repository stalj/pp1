class C():

    def __init__(self,arr):
        self.arr=arr

    def sum(self):
        sum=0
        y=""
        for x in range(len(self.arr)):
            sum+=self.arr[x]
            y+=str(self.arr[x])
            if x+1==len(self.arr):
                y+="="
            else:
                y+="+"
        y+=str(sum)
        return y

c1=C([5,12])
print(c1.sum())
c2=C([6,0,15])
print(c2.sum())