def keypad():
    for i in range(0,9,3):
        for x in range(1,4):
           print(f'{i+x}', end=" ")
        
        print()
keypad()