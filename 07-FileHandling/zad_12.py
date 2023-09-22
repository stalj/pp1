f=open('shopping','w')

x=input("Chcesz dodać kolejny artykuł?")

while x=="Tak":
    f.write(input("Podaj artykuł:"))
    x=input("Chcesz dodać kolejny artykuł?")
    x=x

