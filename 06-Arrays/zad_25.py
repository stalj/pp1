def occurs(number, array):
    for x in array:
        if int(number)==x:
            return True
    return False

a=[9,0,3]

print(occurs(7,a))