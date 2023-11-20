def compare(arr1, arr2):
    print(f'Array 1: {arr1}')
    print(f'Array 2: {arr2}')
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                return True
        return False
    return False

if __name__ == '__main__':
    print("Comparison: arrays are the same" if compare(["water","book","sky"], ["water","book","sky"]) else "Comparison: arrays aren't the same")
    print("Comparison: arrays are the same" if compare([True,False], [True,False,True]) else "Comparison: arrays aren't the same")
    print("Comparison: arrays are the same" if compare([5,3,1], [5,3,1]) else "Comparison: arrays aren't the same")