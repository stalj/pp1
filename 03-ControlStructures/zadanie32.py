a = str(input('Are you interested in computer science? (Y/N): '))
b = str(input('Do you like playing computer games? (Y/N): '))
c = str(input('Do you have an Instagram account? (Y/N): '))
if a == 'Y':
    print('Interested in computer science: Yes')
    if b =='Y':
        print('Playing computer games: Yes')
        if c == 'Y':
            print('Has an Instagram account: Yes')
        elif c == 'N':
            print('Has an Instagram account: No')
    elif b == 'N':
        print('Playing computer games:No')
        if c == 'Y':
            print('Has an Instagram account: Yes')
        elif c == 'N':
            print('Has an Instagram account: No')
elif a == 'N':
    print('Interested in computer science: No')
    if b =='Y':
        print('Playing computer games: Yes')
        if c == 'Y':
            print('Has an Instagram account: Yes')
        elif c == 'N':
            print('Has an Instagram account: No')
    elif b == 'N':
        print('Playing computer games:No')
        if c == 'Y':
            print('Has an Instagram account: Yes')
        elif c == 'N':
            print('Has an Instagram account: No')