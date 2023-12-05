def f(detector: str):
    number = 0
    for iteration in detector:
        if iteration == "+":
            number += 1
            if number == 3:
                break
            if iteration == len(detector):
                break
        elif iteration == "-":
            number -= 1
            if iteration == len(detector):
                break
    if number >= 3:
        return True
    else:
        return False

print(f("+-++-++-+---"))