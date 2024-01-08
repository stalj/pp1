def number(text):
    arr = text.split(' ')
    return len(arr)

def  longest(text):
    arr = text.split(' ')
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if len(arr[j])<len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return ','.join(arr)

def sort_arr(text):
    arr = text.split(' ')
    arr.sort(key = str.lower)
    return ', '.join(arr)

