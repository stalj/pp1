def f(dice):
    count_dice = {}
    for i in dice:
        if i in count_dice:
            count_dice[i]+=1
        else:
            count_dice[i] = 1
    for i, count in count_dice.items():
        if count == max(count_dice.values()):
            return i
        
if __name__ == '__main__':
    print(f('5233165554211'))
    print(f('2133'))