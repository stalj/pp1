file = open("powers.txt", "w")
pow2 = 0
pow3 = 0
st = ""
for i in range(1,11):
    pow2 = i* i
    pow3 = i* i * i
    st = str(i) + " , " + str(pow2) + " , " + str(pow3) + "\n"
    file.write(st)
