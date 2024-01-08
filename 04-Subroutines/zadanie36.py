def f(detector):
    number_of_people = 0
    for i in detector:
        if i == "+":
            number_of_people +=1
        if i == "-":
            number_of_people -=1
        if number_of_people == 3:
            return True
            break
    if number_of_people != 3:
        return False
if __name__ =='__main__':
    print(f('+-+++-+---'))
    print(f('+-+-+-+-'))
    print(f('+-++-+--'))
    print(f('+-++-++-+---'))