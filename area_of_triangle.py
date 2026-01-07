"""When all the sides of triangle are known-a,b,c
semi perimeter =(a+b+c)/2
Area = square root of(s*(s-a)*(s-b)*(s-c)
"""
a=float(input("Enter first side of triangle:"))
b=float(input("Enter second side of triangle:"))
c=float(input("Entre third side of triangle:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is",round(area,4))
print