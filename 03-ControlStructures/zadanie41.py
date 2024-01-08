b = 1
while b <= 3:
    a = str(input('Enter the PIN code: '))
    if a != '0805':
        print('Incorrect...')
    b = b + 1
    if a == '0805':
        print('Correct PIN')
        break
    if b==4:
        print('Sorry, your payment card has been blocked.')

