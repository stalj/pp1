def f(palindrome):
    a = 1
    palindrome = palindrome.replace(" ","").lower()
    for i in palindrome:
        if i == palindrome[-a]:
            a+=1
        else:
            return False
            break
    return True 

if __name__ == '__main__':
    print(f('kajak'))
    print(f('12-11-21'))
    print(f('book'))
