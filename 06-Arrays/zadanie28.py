def median(array):
    n = len(array)
    return (array[n//2-1]/2+array[n//2]/2, array[n//2])[n % 2] if n else None

print(median([6,8,3,1,0,5,7]))
print(median([1,0,9,4,6]))