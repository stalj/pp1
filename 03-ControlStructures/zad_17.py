x=int(input("Wprowadź liczbę:"))
y=int(input("Wprowadź następną liczbę:"))

if x>0 and y>0:
    print(f"Punkt P o współrzędnych P({x},{y}), znajduje się w pierwszej ćwiartce układu współrzędnych")

if x<0 and y>0:
    print(f"Punkt P o współrzędnych P({x},{y}), znajduje się w drugiej ćwiartce układu współrzędnych")

if x<0 and y<0:
    print(f"Punkt P o współrzędnych P({x},{y}), znajduje się w trzeciej ćwiartce układu współrzędnych")

if x>0 and y<0:
    print(f"Punkt P o współrzędnych P({x},{y}), znajduje się w czwartej ćwiartce układu współrzędnych")

if x==0 and y==0:
    print(f"Punkt P o współrzędnych P({x},{y}), znajduje się w środku układu współrzędnych")

