def f(name):
    words = name.split()
    return ''.join(word[0] for word in words)

if __name__ == '__main__':
    print(f('Internet of Things'))
    print(f('For Your Information'))
    print(f('Python'))