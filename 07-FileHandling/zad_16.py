f1=open('zad_15.txt','r',encoding='utf-8')
f2=open('copy.txt','w',encoding='utf-8')

f2.write(f1.read())
f2.close()