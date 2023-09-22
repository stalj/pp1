file=open("ICAO.txt","w")

slownik={
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "w":"Whikey",
    "y":"Yankee",
    "z":"Zulu"
}

for x,y in slownik.items():
    file.write(f"{x} : ")
    file.write(f"{y}\n")
    
file.close()