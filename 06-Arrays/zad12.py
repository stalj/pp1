tablica = [[2, 5, 4], [9, 0, 3]]

print(f"array: {tablica}")
print(f"size of the array: rows = {len(tablica)}, columns = {len(tablica[0])}")
print(f"value 5 from the array: {tablica[0][1]}")
print(f"value 3 from the array: {tablica[1][2]}")

for i in tablica[1]:
    print(i, end = " ")
print()

for i in tablica:
    for j in i:
        print(j, end = " ")
    print()