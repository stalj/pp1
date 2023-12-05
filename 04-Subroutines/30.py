def function(number: str, even: bool):
    odd_sum = 0
    even_sum = 0

    for iteration in number:
        if int(iteration) % 2 == 0:
            even_sum += int(iteration)
        elif int(iteration) % 2 != 0:
            odd_sum += int(iteration)

    if even == True:
        return even_sum
    elif even == False:
        return odd_sum

print(function("20576", True))
