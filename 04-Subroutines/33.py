def function(number):
    if number <= 0:
        return ""
    elif number == 1:
        return "*"
    else:
        return "*" + "/*" * (int(number) - 1)

print(function(106))