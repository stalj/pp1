def f(word):
    if word[::-1] == word:
        return True
    else:
        return False


word = "hannah".lower()

print(f(word))

