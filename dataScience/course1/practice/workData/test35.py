import os
from os.path import basename
def extsort(l):
	s = sorted(l,key= lambda x: x[len(os.path.splitext(x))+1:] )
	return s


print(basename('a.c'))
print(os.path.splitext("a.c")[0])
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
