liczby=[]

x=""
while x!="0":
    x=str(input("Enter number: "))
    if x!="0":
        liczby.append(int(x))

suma=sum(liczby)
mean=(suma/len(liczby))
print(liczby)

print("Quantity: ", len(liczby))
print("Sum: ", suma)
print("Mean: ", mean)