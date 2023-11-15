a = str(input('Enter EAN-13 article number: '))
if len(a) == 13:
    print('Article number is correct')
    if (a[:3] == '590'):
        print('Article manufactured in Poland')
    else:
        print('Article not manufactured in Poland')
else:
    print('Article number is incorrect')