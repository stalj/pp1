even = lambda x: True if x%2 == 0 else False
a = int(input('Enater a number: '))
result = even(a)
print(f'Number {a} is even: {result}')