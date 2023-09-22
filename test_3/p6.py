class C():

    def __init__(self,punkty):
        self.punkty=punkty

    def m(self,a):
        sum=0
        y=0
        for x in self.punkty:
            if self.punkty[y][0]==a[0] and self.punkty[y][1]==a[1]:
                sum+=1
            y+=1
        return sum

c=C([[8,3],[1,8],[-6,4],[1,8]])
c.m([1,8])