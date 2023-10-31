class C:
    def __init__(self,d):
        self.d=d
    def m(self,n):
        a=[]
        s=''
        for key,value in self.d.items():
            if sum(value)/len(value)>=int(n):
                a.append(key)

        return ','.join(sorted(a))


s=C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
s.m(4)
print(s.m(3))
s.m(5)
