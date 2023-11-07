code = (input("Enter EAN-13 article number: "))

if len(code) == 13:
    print("Art is good")
    if len(code) == 13 and code[0:3] == "590":
        print("AYO POLISZ GUT")