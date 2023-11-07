list = ""

for iteration in range(1,8):
    list = ""
    list += f"{iteration} "
    new_number = iteration

    for i in range(6):
        new_number += 7
        if new_number <10:
            list += f" {new_number} "
        else:
            list += f"{new_number} "
    print(list)
