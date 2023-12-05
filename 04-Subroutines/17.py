def different(n1,n2,n3):
    if n1 != n2 and n1 != n3:
        return True
    if n1 == n2 and n1 == n3:
        return False

var1 = input("Gimme number 1: ")
var2 = input("Gimme number 2: ")
var3 = input("Gimme number 3: ")

print(different(var1, var2, var3))