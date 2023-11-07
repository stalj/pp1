class Phone:
    def __init__(self, make, model, storage, color,volume=5):
        self.make = make
        self.model = model
        self.storage = storage
        self.color = color
        self.on = False
        self.silent = False
        self.vibrate = False
        self.volume = volume
    
    def __repr__(self):
        return f"Phone make={self.make}, model={self.model}, storage={self.storage}, color={self.color}"
    
    def turn_on(self):
        self.on = True
        print("Phone is now on")
    
    def turn_off(self):
        self.on = False
        print("Phone is now off")
    
    def set_silent(self):
        self.silent = True
        print("Phone is now in silent mode")
    
    def set_vibrate(self):
        self.vibrate = True
        print("Phone is now in vibrate mode")

    def increase_volume(self):
        if self.on:
            self.volume += 1
            print(f'Volume increased to {self.volume}')
        else:
            print('Turn on the phone first, you dummy')
    
    def decrease_volume(self):
        if self.on:
            self.volume -= 1
            print(f'Volume decreased to {self.volume}')
        else:
            print('Mamma mia, turn on the phone first')

phone1 = Phone(make='Apple', model='iPhone 12', storage='128', color='black')
phone2 = Phone(make='Samsung', model='Galaxy S21', storage='64',color='gray')

print(phone1)
print(phone2)

phone1.turn_on()
phone1.increase_volume()
phone1.turn_off()

phone2.turn_on()
phone2.decrease_volume()
phone2.turn_off()