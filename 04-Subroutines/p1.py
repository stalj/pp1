def f(card, number=10):
    print(f"{card.replace('','')[:2]}{'*' * number}{card.replace('','')[-4:]}")