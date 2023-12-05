def numbers(n):
    list = "1"
    for iteration in range(2,n+1):
        list += f" {iteration}"
    return list

print(numbers(7))