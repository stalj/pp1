n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
def different(n1, n2, n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
if different(n1, n2, n3) == True:
    print(f'Numbers {n1}, {n2}, and {n3} are different')
else:
    print(f"Numbers {n1}, {n2}, and {n3} aren't different")

