humanage=input("Enter the dog's age in human years: ")
dogage=0
while float(humanage)<=2.0:
    for i in range(2):
        dogage=dogage+10.5
    break
else:
    dogage=21+float(humanage)*4
print(dogage)