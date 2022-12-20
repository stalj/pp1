import re
def f(first_letter,last_letter):
    licznik=0
    with open("test.txt","r") as f:
        a=f.readlines()
        result1 = re.findall(rf'\b[{first_letter}]\w+\w+[{last_letter}]\b', str(a), re.I)
        return(len(result1))
print(f('w','d'))