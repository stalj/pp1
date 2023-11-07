def unicode():
    name = input("Enter name: ")
    result = ""
    for i in name:
        result += i+"("+str(ord(i))+ ") "
    
    return result


print(unicode())