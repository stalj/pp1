import re

txt="To be, or not to be, that is the question"
x=["a","e","y","i","o","u"]
y=0

for a in x:
    y=y+len(re.findall(a,txt))


print(y)