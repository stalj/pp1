godziny = input('Podaj liczbę godzin:')
stawka = input('Podaj stawkę godzinową:')
if float(godziny) > 40:
    nadgodziny= float(godziny)-40
    wynagrodzenie=((float(godziny)-nadgodziny)*float(stawka))+(nadgodziny*(float(stawka)*1.5))
else:
    wynagrodzenie=float(stawka)*float(godziny)
print(wynagrodzenie)
