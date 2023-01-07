class C:
    def __init__(self,grades):
        self.grades=grades
    def m(self,n):
        names=[]
        for i,j in self.grades.items():
            if sum(j)/len(j)>=n:
                names.append(i)
        return ','.join(sorted(names))

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})

print(s.m(4))
print(s.m(3))
print(s.m(5))
