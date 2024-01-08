import checking
a = int(input('A number: '))
b = int(input('Enter lower bound of range: '))
c = int(input('Enter upper bound of range: '))
if checking.check(a, b, c):
    print(f'Number {a} in the range <{b},{c}>: yes')
else:
    print(f'Number {a} in the range <{b},{c}>: no')