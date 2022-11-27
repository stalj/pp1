import re

message = 'To be, or not to be, that is the question'
number = re.findall(r'\w+', message)
print(message)
print(f'the number of words: {len(number)}')