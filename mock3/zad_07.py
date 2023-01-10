class C():

    @staticmethod
    def m1(n):
        b=str(n)
        a=""
        for x in b:
            if int(x)%2==0:
                a+=str(x)
        print(a)

    @staticmethod
    def m2(n):
        b=str(n)
        a=0
        for x in b:
            if int(x)<a:
                print(False)
                return
            else:
                a=int(x)
        print(True)

    @staticmethod
    def m3(n):
        a=[0,1,2,3,4,5,6,7,8,9]
        b=str(n)
        for x in b:
            for y in a:
                if int(x)==y:
                    a.remove(y)
                    break
        c=""
        for z in a:
            c+=str(z)
                
        print(c)

C.m1(4231564) 
C.m1(79381) 
C.m2(125579) 
C.m2(4557879)
C.m3(23557)  
C.m3(12340) 