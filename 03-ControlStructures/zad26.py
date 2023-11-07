pin="0805"

for i in range(2):
    haslo=input("Enter your pin: ")
    if haslo==pin:
        print("Correct! ")
        break
    else:
        print("incorrect")
        haslo=input("Enter your pin: ")
        if haslo==pin:
            print("Correct! ")
            break
        else: 
            print("incorrect")
            haslo=input("Enter your pin: ")
            if haslo==pin:
                    print("Correct!")
                    break
            else:
                print("Sorry, your payment card has been blocked.")
                break

