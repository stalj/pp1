def order():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    result = "Numbers in ascending order: "
    if n1 >= n2:
        result += f"{n2}, {n1}"
    else:
        result += f'{n1}, {n2}'

    return result


print(order())