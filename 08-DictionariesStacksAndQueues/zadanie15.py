import json

icaoDict = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
                'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
                'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
                'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
                'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
                'y': 'yankee', 'z': 'zulu'}


file = open('ICAO.txt', 'w') 

for k,v in icaoDict.items():
    file.write(f'{k} {v}\n')
file.close()

