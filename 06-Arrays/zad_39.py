a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

x=0
y=0
dod=1
for i in a[x]:
    a[0][y]=dod
    x=x+1
    y=y+1
    dod=dod+1

x=0
y=0
dod=2
for i in a[x]:
    a[1][y]=dod
    x=x+1
    y=y+1
    dod=2+dod

x=0
y=0
dod=3
for i in a[x]:
    a[2][y]=dod
    x=x+1
    y=y+1
    dod=3+dod

x=0
y=0
dod=4
for i in a[x]:
    a[3][y]=dod
    x=x+1
    y=y+1
    dod=4+dod

x=0
y=0
dod=5
for i in a[x]:
    a[4][y]=dod
    x=x+1
    y=y+1
    dod=5+dod

nr=0
for i in a:
    print(i)
    
    nr+=1