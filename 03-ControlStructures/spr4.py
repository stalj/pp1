def f(palindrom):
    lenght = len(palindrom)
    if palindrom[0] == palindrom[-1]:
        pass

    for i in range(1,int(lenght/2)):
        if palindrom[i] == palindrom[-i+1]:
            pass
        else:
            print ("False")
            return False

f("abcdefgfedcba")
f("radar")
f("abcdecdba")
f("12345432")