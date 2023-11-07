number = int(input("Enter number: "))
prime_numbers = ""

for iteration in range (2, number+1):
    if iteration % 1 == 0 and iteration % iteration == 0:
        prime_numbers += f"{iteration} "

print(prime_numbers)

# NO IDEA