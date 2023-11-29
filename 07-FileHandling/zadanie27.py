import re
message = "To be, or not to be, that is the question"
words = re.findall(r"\b\w+\b", message)
print(words)
print(f"The number of words in the text is: {len(words)}")