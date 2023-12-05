def function(card_number: str):
    # 5290312400019022
    first2 = card_number[:2]
    last4 = card_number[-4:]
    num_of_asterisks = len(card_number) - 6
    return first2 + ("*" * num_of_asterisks) + last4
