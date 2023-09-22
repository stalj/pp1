y="0805"

for i in range(3):
    x=input("Podaj pin:")
    if x==y:
        print("Prawidłowy pin")
        break

if x!=y:
    print("Błędny pin. Karta została zablokowana")
