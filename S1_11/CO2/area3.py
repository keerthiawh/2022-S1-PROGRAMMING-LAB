l=int(input("enter length:"))
b=int(input("enter breadth:"))
rarea=lambda l,b:l*b
print("area of rectangle:",rarea(l,b))
s=int(input("enter side:"))
sarea=lambda s:s*s
print("area of sqaure:",sarea(s))
x=int(input("enter base of triangle:"))
y=int(input("enter height of triangle:"))
tarea=lambda x,y:0.5*x*y
print("area of triangle:",tarea(x,y))
