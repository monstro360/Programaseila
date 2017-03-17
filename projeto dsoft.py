def f(x,y):
	z=x+y
	return z
def g(x,y):
	z=x-y
	return z
def h(x,y):
	z=x*y
	return z
def i(x,y):
	z=x/y
	return z
def j(x,y):
	z=x**y
	return z
def k(x,y):
	z=x**(1/y)
	return z
x=int(input("qual o valor de x?"))
y=int(input("qual o valor de y?"))
f=f(x,y)
g=g(x,y)
h=h(x,y)
i=i(x,y)
j=j(x,y)
k=k(x,y)
print ("adição")
print (f)
print ("subtração")
print (g)
print ("multiplicação")
print (h)
print ("divisão")
print (i)
print ("exponenciação")
print (j)
print ("radiciação")
print (k)
