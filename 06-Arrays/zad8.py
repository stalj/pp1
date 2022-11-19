arr8 = [-15, 8, -31, 47, -2, 19]

maks = arr8[0]
mini = arr8[0]
for i in range(len(arr8)):
    if arr8[i] > maks:
        maks = arr8[i]
    if arr8[i] < mini:
        mini = arr8[i]
            
print(maks)
print(mini)