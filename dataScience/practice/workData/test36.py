def rev():
	s = (open('foo.txt').readlines())
	print(s[::-1])
	return s
print(rev())
