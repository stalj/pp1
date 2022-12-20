filepath = 'countries.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("{}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1