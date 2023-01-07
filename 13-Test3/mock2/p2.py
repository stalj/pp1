class C:
    def __init__(self,ip):
        self.ip=ip
    def m(self):
        a=self.ip.split('.')
        status=False
        for i in a:
            if int(i) in range(0,256):
                status=True
            else:
                status=False
                break
        return status
c=C("23.1.154.0").m()
print(c)
a=C("0.0.257.10" ).m()
print(a)