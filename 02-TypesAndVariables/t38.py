def telephone():
    num = input("Enter phone number: ")
    result  = num[:3]+"-"+ num[3:6]+"-"+num[6:]
    return result


print(telephone())