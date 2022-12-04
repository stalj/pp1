import time
file = open("file.txt")
lines = 0
for i in file:
    print(i, end = "")
    lines = lines +1
    if lines == 5:
        time.sleep(5)
        lines = 0