def function(x,y):
    number = 0

    for iteration in range(x,y + 1):
        if iteration < 0 and iteration % 2 == 0:
            number += 1
        else:
            continue
    return number


print(function(-1,11))