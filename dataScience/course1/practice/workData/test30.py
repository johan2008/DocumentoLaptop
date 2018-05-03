def dups(l):
	s2 = []
	s = list(l)
	for i in range(len(l)):
		v = 0
		print(" -- ",i)
		for j in range(i+1,len(l)):
			if l[i] in s[j:len(l)]:
				v = 1
				break
		if v==1 :
			print(i)
			s2.append(l[i])

	return s2

print(dups([1,2,1,3,2,5]))
