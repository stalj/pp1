class Bank():
    def __init__(self, number):
        self.number = number
        self.balance = 0.00
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount_w):
        if self.balance - amount_w >=0:
            self.balance-=amount_w
        else:
            print("Insufficient funds on the account")
    def show_status(self):
        print(f"Bank account no: {self.number}")
        print(f"Balance: PLN {self.balance}")

acc = Bank("12 3456 5555 9090 1111 0000 7722")
acc.show_status()
acc.deposit(25.00)
acc.show_status()
acc.withdraw(37.00)
acc.show_status()
acc.withdraw(14)
acc.show_status()


