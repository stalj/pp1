class C:
    def __init__(self,calkowita):
        self.calkowita=calkowita
    def __str__(self):
        if self.calkowita>=0:
            return '*'*self.calkowita
        else:
            return ''
obj = C(-10)


obj = C(0)
print(obj)

obj = C(5)
print(obj)

obj2 = C(3)
print(obj2)

