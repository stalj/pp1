number = int(input("Enter number: "))

bin_number = bin(number)
hex_number = hex(number)

print(f"Binary: {bin_number}, Hex {hex_number}")
print(type(bin_number))