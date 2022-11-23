while True:
    with open('wiki.txt','r', encoding='utf-8') as f:
       for x in range(5):
        print(f.readline())
    qw = input('')
    if qw == '.':
      break
    elif qw == '':
        continue

