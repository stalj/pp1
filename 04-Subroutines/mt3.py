def f(amount_to_pay):
    if amount_to_pay%5 == 0:
        print (int(amount_to_pay/5))
    elif (amount_to_pay - int((amount_to_pay/5)*5)) %2 == 0:
        print(int(amount_to_pay/5) + ((amount_to_pay - int((amount_to_pay/5)*5)))/2)
    else:
        print(int(amount_to_pay/5) + ((amount_to_pay - int((amount_to_pay/5)*5)))/2 +1)

f(23)
f(8)
f(2)
f(0)