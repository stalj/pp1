a = int(input('Enter decimal number: '))
d = a
binary_digits = [] 
if a == 0:
    binary_digits.append(str(a))
while a>0:
    reminder = a%2
    a = a//2
    binary_digits.append(str(reminder))
print (f'{d}(10) = {''.join(reversed(binary_digits))}(2)')
    