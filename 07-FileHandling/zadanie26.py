import re

with open('text.txt') as file:
 text = re.findall(r'\w{6,}' , file.read())
print(*text, sep='\n')
