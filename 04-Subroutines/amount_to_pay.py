def f(amount_to_pay):
    coins_5_pln = 0
    coins_2_pln = 0
    coins_1_pln = 0
    while amount_to_pay >= 5:
        amount_to_pay -= 5
        coins_5_pln += 1
    while amount_to_pay >= 2:
        amount_to_pay -= 2
        coins_2_pln += 1
    coins_1_pln = amount_to_pay
    total_coins = coins_5_pln + coins_2_pln + coins_1_pln
    return total_coins