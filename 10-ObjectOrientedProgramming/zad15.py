import random

class thermometer():

    temp = random.randrange(34,42) + random.randrange(11)*0.1
    message1 = ""
    status = False


    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False
        
    def __init__(self):
        if self.temp >= 37:
            self.message1 = "fever"
        else: 
            self.message1 = " "
        if self.temp >= 41:
            self.message1 += " CRITICAL TEMPERATURE"

    def show_temp(self):
        if self.status == True:
            print(f"Temperature: {self.temp}C {self.message1}")
        else:
            print("off")