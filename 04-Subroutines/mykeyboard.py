def read_number():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return read_number()

if __name__ == "__main__":
    num1 = read_number()
    num2 = read_number()
    
    total = num1 + num2
    print("The sum of the two entered numbers is:", total)
