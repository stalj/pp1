from cgitb import reset


class C():

    @staticmethod
    def m(n):
        result=""
        n=str(n)
        for x in n:
            if int(x)%2==0:
                result+=x
        if result=="":
            return 0
        return int(result)

C.m(791)