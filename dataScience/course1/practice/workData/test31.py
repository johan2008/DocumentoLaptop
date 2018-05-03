def group(l,size):
	#s1=[]
	s2=[]
	for i in range(0,len(l),size):
		print(i)
		s1 = []
		for j in range(i,i+size):
			print(j)
			s1.append(l[j])
		s2.append(s1)
	#print(i)
	return s2

print(group([1,2,3,4,5,6,7,8,9],3))
