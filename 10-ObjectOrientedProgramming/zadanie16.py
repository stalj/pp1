class Phone():
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        self.power_status = False
    def __str__(self):
        return f"{self.color} {self.brand} {self.model} {'is on' if self.power_status == True else 'is off'}"
    def is_on(self):
        self.power_status = True
    def is_off(self):
        self.power_status = False
    def calling(self, number):
        if self.power_status:
            print(f'{self.color} {self.brand} {self.model} is currently calling number: {number}...')
        else:
            print("The phone is off")
phone1 = Phone("Black", "Samsung", "Galaxy S2")
phone2 = Phone("Blue", "Xiaomi", "Note 8T")

print(phone1)
phone1.is_on()
print(phone1)
phone1.calling('514556695')
phone1.is_off()
print(phone1)

print(phone2)
phone2.is_on()
print(phone2)
phone2.calling('514556695')
phone2.is_off()
print(phone2)

    