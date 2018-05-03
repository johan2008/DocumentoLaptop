#function a utilizar con map() y reduce
def suma(n,m):
	return n+m

#funcion a utilizar con filter()
def filtrar(n):
	return (n=='o')

li = [1,-2,1,-4]
lo = [5,3,6,7]
s = "hola mundo"



print(map(lambda n,m: n+m, li,lo))
