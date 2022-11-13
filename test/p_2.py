def f(number1,number2,operator):
    if operator=="+":
        return(number1+number2)
    elif operator=="-":
        return(number1-number2)
    elif operator=="*":
        return(number1*number2)
    elif operator=="**":
        return(number1**number2)
    elif operator=="%":
        return(number1%number2)

print(f(2,3,"*"))