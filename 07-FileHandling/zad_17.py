f1=open('zad_15.txt','r',encoding='utf=8')
f2=open('copyline.txt','w',encoding='utf-8')

for line in f1:
    f2.write(f1.readline() + "\n")

f2.close()