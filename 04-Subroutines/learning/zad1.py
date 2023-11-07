def f(card_number):
    str=""
    for i in card_number:
        str=card_number[:2]+12*"*"+card_number[-4:]
    return str
print(f("529031240001902"))

