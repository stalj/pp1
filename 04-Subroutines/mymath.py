def read_number():
    x=int(input("Podaj liczbę w przedziale <1;9>:"))
    return x

def generate_number():
    import random
    a=random.randint(1, 9)
    return a