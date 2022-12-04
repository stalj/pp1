array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = ""
for i in array:
    if int(len(longest)) < int(len(i)):
        longest = i
    else: 
        pass

print(f"names {array}")
print(f"Longest name: {longest}")
