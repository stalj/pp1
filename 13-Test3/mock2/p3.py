class C:
    def __init__(self,tel):
        self.tel=tel

    def m(self):
        status=False
        a=set(self.tel)
        if len(a)!=len(self.tel):
            return True
        else:
            return False

print(C(["111222333", "123123123", "111222333"]).m())
print(C(["111222333", "123123123","321321321","333222111"]).m())