def istrcmp(s1, s2):
	c1 = s1.upper();
	c2 = s2.upper();
	if c1 == c2:
		return True
	else:
		return False

print(istrcmp('python','Python'))
print(istrcmp('a','b'))
