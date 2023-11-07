pin_code = "0805"
attempt = 1



while attempt <= 4:
    if attempt == 4:
        print("Sorry, your payment card has been blocked.")
        break

    var = input("Enter the PIN code: ")
    if var != pin_code:
        print("Incorrect...")
        attempt += 1

    if var == pin_code:
        print("Correct")
        break
