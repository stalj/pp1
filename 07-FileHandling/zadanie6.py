file = open('countries.txt','r', encoding='utf-8')  #cd \07-fileshanding\
file_content = file.read()
print( file_content )
file.close()
