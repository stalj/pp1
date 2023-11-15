def f(card_number):
    card_number = str(card_number)
    return card_number[0:2] + 10*'*'+ card_number[12:16]

if __name__ == '__main__':
    print(f(5290312400019022))