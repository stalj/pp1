import re

message = 'To be, or not to be, that is the question'
number = re.findall('[aoeiyu]',message)
print(number)
print(len(number))