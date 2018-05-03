import collections

def word_frecuency(words):
	frecuency = {}
	for w in words:
		frecuency[w] = frecuency.get(w,0)+1
	return frecuency


f = open('foo.txt')
s = f.read().split()
#print(word_frecuency(s))
res = word_frecuency(s)
d = collections.Counter(res)
for word, count in d.most_common(2):
	print(word," : ",count)
