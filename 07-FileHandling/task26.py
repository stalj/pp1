import re
file = open("file.txt", "r")
text = file.read()
file.close()
sixLettersOrMore = re.findall(r'w{6}',text) 
print(sixLettersOrMore)