class TV():
    def __init__(self):
        self.is_on = False
        self.channel_number = 1
        self.channel_list = []
        self.volume = 0
    def set_channel(self, new_channel_no):
         self.channel_number = new_channel_no
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_number}', end="")
            if len(self.channel_list)>0 and len(self.channel_list)>=self.channel_number:
                 print(f'({self.channel_list[self.channel_number-1]})', end="")
            print(f", VOLUME: {self.volume}")
        else:
            print("TV is off")
    def set_channels(self, channel_list):
         self.channel_list = channel_list
    def show_channel(self):
        if len(self.channel_list) == 0:
            print('There is no avaliable channels, please set the channels.')
        else:
            print("Channel list:")
            for i in range(len(self.channel_list)):
                print(f'{i+1}. {self.channel_list[i]}')
    def volume_increase(self):
        if self.volume < 10:
            self.volume+=1
        else:
            print("Volume cannot be further increased due to getting to the top of the volume scale")
    def volume_decrease(self):
        if self.volume > 0:
            self.volume-=1
        else:
            print("Volume cannot be further decreased due to getting to the bottom of the volume scale")

tv = TV()
tv.show_status()
tv.turn_on()
tv.show_channel()
tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv.show_channel()
tv.set_channel(2)
tv.show_status()
tv.volume_increase()
tv.show_status()
tv.volume_increase()
tv.show_status()
tv.volume_increase()
tv.show_status()
tv.volume_decrease()
tv.show_status()
tv.turn_off()
tv.show_status()
