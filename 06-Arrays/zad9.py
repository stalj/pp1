tablica = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest = tablica[0]

for i in range(len(tablica)):
    if len(tablica[i]) > len(longest):
        longest = tablica[i]

print(f"Names: ", end = "")
for i in range(len(tablica)):
    print(tablica[i], end = ", ")

print()
print(f"Longest: {longest}")