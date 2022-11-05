def get_hidden_card(card, number=10):
    print(f"{card.replace('', '')[:2]}{'*' * number} {card.replace('', '')[-4:]}")
 
get_hidden_card('5290312400019022')