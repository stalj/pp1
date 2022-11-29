binary=[]
x=int(input("Podaj liczbę:"))
while x!=0:
    if x%2==0:
        binary.append(0)
        x=x/2
    else:
        binary.append(1)
        x=(x-1)/2

for i in range(len(binary)-1,-1,-1):
    print(binary[i],end=" ")