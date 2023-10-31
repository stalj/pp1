from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA


fibonaci=[0,1]
licznik=0
n1=0
n2=1

for i in range(2,51):
        fibonaci.append(fibonaci[i-1]+fibonaci[i-2])
print(fibonaci)

    