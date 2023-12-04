# 변수 정의

a="1"
b="2"
c="3"
x=" "
y=" "

print("{},{},{},{},{}".format(a,x,b,y,c))

b = x
x = 2

print("{},{},{},{},{}".format(a,x,b,y,c))

a = b
b = 1

print("{},{},{},{},{}".format(a,x,b,y,c))

c = y
y = 3

print("{},{},{},{},{}".format(a,x,b,y,c))

b = c
c = 1

print("{},{},{},{},{}".format(a,x,b,y,c))

y = b 
b = 3

print("{},{},{},{},{}".format(a,x,b,y,c))

b = a
a = 3

print("{},{},{},{},{}".format(a,x,b,y,c))

x = b
b = 2

print("{},{},{},{},{}".format(a,x,b,y,c))
