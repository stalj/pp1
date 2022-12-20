import re

txt="To be, or not to be, that is the question"
vovel=["A", "E", "I", "O", "U", "W", "Y","a","e","i","o","u","w","y"]
vowels = re.findall('[aeiou]', txt, re.IGNORECASE)
print(len(vowels))