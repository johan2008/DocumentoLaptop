def unique(l):
	s = []
	s.append(l[0])
	for i in l:
		if l[i] in s:
			print(" -- ")
		else:
			s.append(l[i])
	return s

print(unique([1,2,1,3,2,5]))
