def f(card_number):
   card_number= card_number[0:2] + "**********" + card_number[12:16]
   print(card_number)

f("5290312400019022")