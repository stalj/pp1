import re
text = "To be, or not to be, that is the question"
number_of_words = re.findall(r'\w+' ,text)
print(len(number_of_words))
