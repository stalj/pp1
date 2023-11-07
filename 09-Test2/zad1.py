cards={
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "A":10,
    "K":10,
    "Q":10,
    "J":10
}

def f(player1, player2):
    licznik1=0
    licznik2=0
    for i in player1:
        if i in cards:
            licznik1=licznik1+cards[i]
    for j in player2:
        if j in cards:
            licznik2=licznik2+cards[j]
    if  licznik1>licznik2:
        return True
    else:
        return False
print(f("AJ972","AQT72"))
print(f("9532","K8"))
print(f("987","AT4"))
