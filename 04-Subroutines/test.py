dice = "1114444111"
if dice == "":
    print (None)  

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

print (max_roll)
