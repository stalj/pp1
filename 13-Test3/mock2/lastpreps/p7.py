class C:
    @staticmethod
    def m1(n):
        num=''
        for i in str(n):
            if int(i)%2==0:
                num=num+str(i)
        return int(num)
    def m2(n):
        p=None
        for i in str(n):
            if p is not None and p>int(i):
                return False
            p=int(i)
        return True
    def m3(n):
        a=[0,1,2,3,4,5,6,7,8,9]
        b=[]
        c=[]
        for i in str(n):
            b.append(int(i))
        for i in a:
            if i not in b:
                c.append(i)
        s=''
        for i in sorted(c):
            s=s+str(i)
        print(b)
        print(set(b))
        print(c)
        print(s)

#print(C.m1(4231564))
#print(C.m2(1234455))
#print(C.m2(54321))
print(C.m3(855461))