f = str(input("File name: "))
count = 0
with open(f,"r") as f:
    for line in f:
        count+=1
print(f"Number of lines: {count}")