def cumulative_product(l):
	s = list(l);
	for i in range(len(l)):
		for j in range(i):
			l[i] = l[i]*s[j]
	return l

print(cumulative_product([1,2,3,4]))
