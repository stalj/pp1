x=[4,36,12,28,9,44,5]
y=[5,1,36]

for j in x:
    if j not in y:
        print("Appear in x, not in y: ", j)
for h in y:
    if h not in x:
        print("Appear in y, not in x: ", h)