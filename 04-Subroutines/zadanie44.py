def f(password):
    sum = 0
    character_count = {}
    for i in password:
        if i in character_count:
            character_count[i]+=1
        else:
            character_count[i] = 1
    for i, count in character_count.items():
        if count ==1:
            sum +=1
    if sum < 6:
        return False
    else:
        return True

if __name__ =='__main__':
    print(f('ax15'))
    print(f('book123'))
    print(f('A2water3'))
    print(f('qwerty'))
    print(f('ghjklopg'))