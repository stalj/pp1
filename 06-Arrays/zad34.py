x=[2,3,4]
y=[1,5,6,8,9,3,4,2,10,13,15]

for i in x:
    if i in y:
        x=1
        continue
    else:
        x=0
        break
if x==1:
    print(True)
else: 
    print(False)