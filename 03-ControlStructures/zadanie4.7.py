def computegrade():
    x = input('Podaj wartość: ')
    if float(x) > 0 and float(x) <= 1.0:
        if float(x) >= 0.6 and float(x) < 0.7:
            print('3,5')
        elif float(x) >= 0.7 and float(x) < 0.8:
            print('4,0')
        elif float(x) >= 0.8 and float(x) < 0.9:
            print('4,5')
        elif float(x) >= 0.9:
            print('5,0')
        elif float(x) < 0.5:
            print('2,0')
    else:
      print('Niepoprawna wartość') 

computegrade()