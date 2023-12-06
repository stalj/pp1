class Phone():
    def __init__(self, brand, color, weight):
        self.brand = brand
        self.color = color
        self.weight = weight
        self.is_on = False
        self.missed_calls = 0
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def missing_calls(self,missed):
        self.missed_calls = missed
phone = Phone(
    "iPhone", "black", "204g"
)  
print(f"My phone's brand is {phone.brand}. ", end ="")
print(f"It's {phone.color}. ", end = "")
print(f"It weights {phone.weight}.")

phone.on()
phone.missing_calls(15)

if phone.is_on:
    if phone.missed_calls == 0:
        print("I have no missed calls.")
    else:
        print(f"I have {phone.missed_calls} missed calls! My mum will kill me!")
else:
    print("My phone is off.")