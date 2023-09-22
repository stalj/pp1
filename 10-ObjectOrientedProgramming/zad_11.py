class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_on(self):
        self.is_on=True
    
    def turn_off(self):
        self.is_on=False

    # def channel_no(self):
    #     self.

    def show_status(self):
        if self.is_on==True:
            print('TV is on',)
            print(f'kanal to: {self.channel_no}')
        else:
            print('TV is off')
            
    def change_channel(self,num):
        self.channel_no=num

    def set_channels(self,lista):
        for i in lista:
            self.channels.append(i)
        
    def show_channels(self):
        print('dostepne kanaly', self.channels)

tv=TV()
tv.set_channels(['TVP1',"TVP2",'Polsat','TVN','Filmbox','Discovery'])
tv.show_status()
tv.turn_on()
tv.change_channel(1)
tv.show_status()
tv.change_channel(3)
tv.show_status()
tv.change_channel(4)
tv.show_status()
tv.change_channel(5)
tv.show_status()
tv.change_channel(6)
tv.show_status()
tv.change_channel(8)
tv.show_status()
tv.show_channels()