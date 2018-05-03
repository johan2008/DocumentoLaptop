def cumulative_sum(l):
	ant =list( range(len(l)))
	#ant[0] = 5

	print("primer:  ",ant)
	for i in range(len(l)):
		s = l[i]
		for j in range(i):
			#print("i ",i)
			#print("j" ,j)
			#l[i]+=ant[j]
			s+=l[j]
		ant[i] = s
		print(" -- ")
	print("las  ",ant)
	return l

print(cumulative_sum([1,2,3,4]))
