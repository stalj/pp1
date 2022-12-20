import re

txt="To be, or not to be, that is the question"

letters = re.findall('[qwertyuiopasdfghjklzxcvbnm]', txt, re.IGNORECASE)
print(len(letters))
words=re.findall('\w+',txt,re.IGNORECASE)
print(len(words))