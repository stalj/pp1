number=0
first = str(number)[0]
for digit in str(number):
    if digit == first:
        continue
    else:
        return False
return True