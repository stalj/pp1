def password():
    password = input('Enter password: ')
    if len(password) < 8:
        reslt = False
    else:
        reslt = True
    result = f"Password is valid: {reslt}"
    return result

print(password())