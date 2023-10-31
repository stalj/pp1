import sys
class Stack ():
    def __init__(self):
        self.items=[]
    def push (self,item):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
    def size(self):
        return len(self.items)
s=[]
dec=int(input("Podaj liczbe wariacie: "))

while(dec>0):
    s.append(int(dec%2))
    dec=int(dec/2)


a=len(s)-1
while(a<=len(s) and a>=0):
    print(s[a], end=" ")
    a=a-1