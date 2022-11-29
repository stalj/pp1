countries = [{
    'country' : 'Poland',
    'popularity' : '37,38 mil',
},
{
     'country' : 'Belarus',
    'popularity' : '9,255 mil',
},
{
     'country' : 'Spane',
    'popularity' : '47,163 mil',
},
{
     'country' : 'Italy',
    'popularity' : '59,3 mil',
},
{
    'country' : 'Irlandia',
    'popularity' : '5,123 mil',
}]

i=0
while i<len(countries):
    for k,v in countries[i].items(): #k-klucz,v-value
        print(v, end = ' ')
    print()
    i+=1