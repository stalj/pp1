amount_of_numbers = 0
sum = 0

while True:
    number = int(input("Enter number: "))
    if number != 0:
        sum += number
        amount_of_numbers += 1
    elif number == 0:
        break

print(f"RESULT: Quantity={amount_of_numbers}, Sum={sum}, Mean={sum/amount_of_numbers}")



