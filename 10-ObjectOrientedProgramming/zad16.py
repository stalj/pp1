class BANK:
    def __init__(self,number):
        self.balance=0
        self.number=number
    def depo(self, amount):
        self.a=amount
        self.balance+=self.a
    def wd(self, amount):
        self.w=amount
        if self.w<=self.balance:
            self.balance-=self.w
        else:
            print("mmm puuuuu")
    def disp(self):
        print(f"Bank acc with no: {self.number}, have this balance: {self.balance}")


acc=BANK('12 3456 5555 9090 1111 0000 7722')
acc.disp()
acc.depo(100.50)
acc.wd(50)
acc.disp()
