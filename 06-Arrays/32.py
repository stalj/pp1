arr = [15, 38, 7, 23, 14]
num = int(input("Giveth me a numbuh: "))


def occurs(arr, num):
    yeah_there_is = False
    for i in arr:
        if i == num:
            yeah_there_is = True
        else:
            continue
    return yeah_there_is

print(occurs(arr,num))
