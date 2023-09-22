import re

txt="To be, or not to be, that is the question"
sum=0
a=re.split("\s",txt)

for x in a:
    sum+=1

print(sum)