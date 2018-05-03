def reverse2():
	s = open('foo.txt').readlines()
	for i in range(len(s)):
		print(s[i][::-1])


reverse2()
