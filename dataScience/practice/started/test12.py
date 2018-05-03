def count_digits(n):
	c = 0
	while n/10:
		c+=1
		n =int( n/10)
		#print(n)
	return c


print(count_digits(123))
print(count_digits(123456))
print(count_digits(2))
