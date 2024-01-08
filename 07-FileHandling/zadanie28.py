import re
with open('randomtext.txt', "r") as file:
    for line in file:
        line = line.rstrip()
        x = re.findall(r'\b\w+\b', line)
        for i in x:
            if len(i) >=6:
                print(i)