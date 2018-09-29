'''def add():
	a=10
	b=20
	c=a+b
	print(c)
add()'''

def add():
	a=10
	b=20
	c=a+b
	return(c)
d=add()
print(d)	

'''def sub():
	a=15
	b=30
	c=b-a
	print(c)
sub()'''

def sub():
	a=15
	b=30
	c=b-a
	return(c)
d=sub()
print(d)
	
def add(a,b):
	return a+b
def sub(a,b):
	return a-b

i=int(input("enter number A:"))
j=int(input("enter number b:"))		

d=add(i,j)
print("addition:",d)

print("substraction",sub(i,j))

print("addition:",d)

print("substraction",sub(i,j))

dl319@soetcse:~/tanuja$ python3 tan.py
30
dl319@soetcse:~/tanuja$ python3 tan.py
30
-15
dl319@soetcse:~/tanuja$ python3 tan.py
30
15
dl319@soetcse:~/tanuja$ python3 tan.py
enter number A:12
enter number b:23
addition: 35
substraction -11
