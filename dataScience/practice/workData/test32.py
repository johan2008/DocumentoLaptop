def lensort(l):
	s =sorted(l,key =lambda x:len(x))
	return s

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
