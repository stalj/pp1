
a= [[-38, 19],[5,40],[-7,11],[29,16]]

x=0
najmniejsze=[]
for i in range(4):
    najmniejsze.append(min(a[x]))
    x=x+1

y=0
najwieksze=[]
for i in range(4):
    najwieksze.append(max(a[y]))
    y=y+1    

m=min(najmniejsze)
w=max(najwieksze)
j=0
o=0
q=1
for i in a:
    if m in i:
         print(m,'row',j)
    if w in i:
        print(w,'row',j)
    j=j+1