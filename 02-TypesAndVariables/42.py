number = input("Enter number: ")

dec_number = None

for num in number:
    power = len(number) - 1
    intnum = int(num)
    intnum**power += dec_number

