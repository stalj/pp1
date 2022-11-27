def mediana(arr):
    sorted_arr=sorted(arr)
    n=len(arr)
    if n%2==0:
        x=n//2-1
        return (sorted_arr[x]+sorted_arr[x+1])/2
    else:
        y=n//2
        return sorted_arr[y]

a=[1,0,9,4,6,]
b=[6,8,3,1,0,5,7]
print(mediana(b))