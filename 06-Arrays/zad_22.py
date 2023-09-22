a1=[4,36,12,28,9,44,5] 
a2=[5,1,36]

# x=0
# for i in a1:
#     for y in a2:
#         if a1[x]==y:
#             print(a1[x],end=' ')
#     x=x+1

x=0
for i in a1:
    if i not in a2:
        print(i,end=' ')