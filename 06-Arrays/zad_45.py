def convert(a):
        a[0]=a[0]+a[1]
        a.remove(a[1])
        return a


arr=[[2,3],[1,5]]

print(convert(arr))

arr=[[5, 0, 3, 7, 5,],[9, 0, 9, 1, 2,]]

print(convert(arr))