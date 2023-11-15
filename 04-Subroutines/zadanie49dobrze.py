def f(dice):
    if dice == "":
        return None  

    max_roll = None
    max_count = 1
    current_roll = dice[0]
    current_count = 1

    for i in range(1, len(dice)):
        if dice[i] == current_roll:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_roll = current_roll
        else:
            current_roll = dice[i]
            current_count = 1

    return max_roll

if __name__ == "__main__":
    print(f('"5233165554211"'))
    print(f('2133'))
    print(f("111144444111"))
    print(f('21'))