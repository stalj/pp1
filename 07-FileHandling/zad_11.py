a=['Harry Potter','Hobbit','Władca pierścieni','Avatar','Gwiezdne Wojny']

f=open('film.txt','w',encoding='utf-8')
for x in a:
    f.write(x+"\n")

f.close()