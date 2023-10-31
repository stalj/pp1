class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on==True:
            try:
                print("TV is on, channel", self.channel_no, "(",self.channels[self.channel_no-1],")")
            except:
                print("TV is on, channel", self.channel_no)
        elif self.is_on==False:
            print("TV is off")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        for i in channels_list:
            self.channels.append(i)

    def show_channels(self):
        print("Available channels:", self.channels)

tv=TV()
tv.set_channels(['TVP1',"TVP2",'Polsat','TVN','Filmbox','Discovery'])
tv.show_status()
tv.turn_on()
tv.set_channel(1)
tv.show_status()
tv.set_channel(3)
tv.show_status()
tv.set_channel(4)
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.set_channel(6)
tv.show_status()
tv.set_channel(8)
tv.show_status()
tv.show_channels()