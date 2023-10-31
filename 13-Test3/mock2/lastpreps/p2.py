def f(arr):
    for i in range(0, len(arr)):
        if not all(len(arr)==len(i) for i in arr):
            return False
        for j in range(0,len(arr[i])):
            if arr[i][j]==(i+1)*(j+1):
                return True
            else:
                return False
def main():
    #print()
    print(f([[1,2,3],[2,4,6],[3,6,9]]))
    print(f([[1,2],[2,4]]))
    print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
    print(f([[1,2],[3,6]]))
    print(f([[1,2,3],[2,4,6]]))
    print(f([[1,2,3],[2,4,6],[3,6,9,12]]))
if __name__ == "__main__":
    main()

