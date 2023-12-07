def a(arr):
    arr.remove(max(arr))
    return max(arr)


def b(arr):
    maxi = max(arr)
    mini = min(arr)
    return maxi - mini


def c(arr):
    mid = len(arr)
    var = int(mid / 2)
    if mid % 2 == 0:
        return int((arr[var] + arr[var-1]) / 2)
    elif mid % 2 != 0:
        return arr[var]


def d(arr):
    maxi = max(arr)
    mini = min(arr)
    return [mini, maxi]


def e(arr):
    var = f"{arr[0]}"
    for index in range(len(arr)-1):
        var += f"-{arr[index + 1]}"
    return var
