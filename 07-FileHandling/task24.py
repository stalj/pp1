import re
text = "To be, or not to be, that is the question"
volwes = re.findall(r'a|e|i|o|u|y',text)
print(len(volwes))