fname = input()
f = open(fname,'r')
print(f.closed)
f.close()
print(f.closed)