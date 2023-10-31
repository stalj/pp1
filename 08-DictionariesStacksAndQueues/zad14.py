ipa={
    "a":"alfa",
    "b":"bravo",
    "c":"charlie",
    "d":"delta",
    "e":"echo",
    "f":"foxtrot",
    "g":"golf",
    "h":"hotel",
    "i":"india",
    "j":"juliett",
    "k":"kilo",
    "l":"limo",
    "m":"mike",
    "n":"november",
    "o":"oscar",
    "p":"papa",
    "q":"quebec",
    "r":"romeo",
    "s":"sierra",
    "t":"tango",
    "u":"uniform",
    "v":"victor",
    "w":"whiskey",
    "x":"x-ray",
    "y":"yankee",
    "z":"zulu",
}

name=str(input("Enter name: ")).lower()

for i in name:
    print(ipa[i])
