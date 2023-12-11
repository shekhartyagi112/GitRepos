

var1=30
var2=40
var3= var1+var2
print(var3)


#2)Python Program to subtract two integer values.

var1=20
var2=10
var3= var1-var2
print(var3)

#3)Python program to multiply two numbers.

var1=20
var2=10
var3= var1*var2
print(var3)

#4)Python program to repeat a given string 5 times.

str1 = "Python"
print(str1*5)

#5)Python program to get the Average of given numbers.

var1 = 40
var2 = 50
var3 = 30

var4 = ((var1+var2+var2)/3)
print(var4)

#6)Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2
# n = Number of values

list1 = [45, 60, 61, 66, 70, 77, 80]
list1.sort()
i= (len(list1))/2
print("Median: ", list1[int(i)])

#7)Python program to print the square and cube of a given number.
# Input : num1 = 9

num1 = 9
num2 = num1**2
num3 = num1**3
print(num2, num3)

#8)Python program to interchange values between variables.

var1 = 10
var2 = 20
var1, var2 = var2, var1

print(var1, var2)


# 9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)

import math
side1 = 5
side2 = 4

hypo = side1**2+side2**2
print("Hypotenious side: ",math.sqrt(hypo))

# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
a = 2
b = 3
lhs = (a+b)**2
rhs = a**2+b**2+2*a*b
print(lhs, rhs)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab

a = 4
b = 8
lhs = (a-b)**2
rhs = a**2+b**2-2*a*b
print(lhs, rhs)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)

a = 10
b = 5
lhs = a**2-b**2
rhs = (a+b)*(a-b)
print(lhs, rhs)


# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a = 4
b = 5
lhs = (a+b)**3
rhs = a**3+3*a*b*(a+b)+b**3
print(lhs, rhs)

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
a = 10
b = 8
lhs = (a-b)**3
rhs = a**3-3*a**2*b+3*a*b**2-b**3
print(lhs, rhs)

# 15). Python program to calculate the area of the square.
# Formula : area = a*a
area=10
output=a*a
print("area of the square :",output)

# 16). Python program to calculate the area of a circle.
# Formula = PI*r*r
# r = radius
# PI = 3.14
r=2
PI = 3.14
radies = PI*r*r
print("Area of the circle :" ,radies)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
a=3
ac=6*a*a
print("Area of the cube :",ac)

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
r=2
PI = 3.14
h=3
acy= 2*PI*r*h + 2*PI*r*r
print("Area of the cylinder :",acy)

# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

lhs=153
rhs=1*1*1 + 5*5*5 + 3*3*3
print("Armstrong number:" ,lhs,rhs)

# 20). Python program to calculate simple interest.
# Formula = P+(P/r)*t
# P = Principle Amount
# r = Anual interest rate
# t = time

p = 1000
r = 10
t = 2

amount = p+(p/r)*t

print("Amount payable: ",amount)