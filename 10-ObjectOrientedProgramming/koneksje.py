class koneksjelista:
    def __init__(self):
        self.contactlist=[]
    def add_new(self,addContact):
        self.contactlist.append(str(addContact))
    def disp(self):
        for i in self.contactlist:
            print(i)