def different(n1,n2,n3):
    return(n1 != n2 and n1 !=n3 and n2 != n3) 

n1 = int(input("Enter first num: "))
n2 = int(input("Enter second num: "))
n3 = int(input("Enter third num: "))
print(different(n1,n2,n3))