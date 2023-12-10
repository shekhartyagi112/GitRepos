''
#Python program Add to Integer values:
var1=10
var2=30
var3=var1+var2
print(var3)

#Python program to Sub two integer values:
var1=23
var2=20
var3=var1-var2
print(var3)

#3)Python program to multiply to number
mul1=20
mul2=30
ans=mul1*mul2
print(ans)

#4)Python program to repeat a give string 5 times.
str1="Python"
print(str1*5)


#5)Python program to get the average of give numbers.
var1 = 10
var2 = 50
var3 = 40
var4 =((var1+var2+var3)/3)
print(var4)

#6)Python program to get the median of given numbers.
#Note: all the number should be arranged in ascending order
#Formula :(n+1)/2
#n=Number of values

list1 = [45,60,61,65,70,77,80]
list1.sort()
i=(len(list1))/2
print("Median: ", list1[int(i)])

print("_" *50)
#7)Python program to print the square and cube of a given number.
# Input : num1 = 9

num1 = 10
num2 = num1**2
num3 = num1**3
print(num2, num3)


#8)Python program to interchange values between variables.
print("_" *50)
var1=10
var2=20
var1, var2 =var2, var1
print(var1, var2)

# 9)Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
print("_" *50)
import math
side1=5
side2=4

hypo=side1**2+side2**2
print("Hypotenious side: ", math.sqrt(hypo))
print("_" *50)

# 10)Python program to solve the given math formula.
#formula : (a+b)2 =a2 +b2 2ab
a=2
b=3
lhs=(a+b)**2
rhs=a**2+b**2+2*a*b
print(lhs, rhs)
print("_" *50)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab

a = 2
b = 3
lhs = (a-b)**2
rhs = a**2+b**2-2*a*b
print(lhs, rhs)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)

print("_" *50)
a=2
b=5
lhs=a**2-b**2
rhs=(a+b)*(a-b)
print(lhs,rhs)

# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
print("_" *50)
a = 4
b = 5
lhs = (a+b)**3
rhs = a**3+3*a*b*(a+b)+b**3
print(lhs, rhs)

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
print("_" *50)
a = 10
b = 8
lhs = (a-b)**3
rhs = a**3-3*a**2*b+3*a*b**2-b**3
print(lhs, rhs)

# 15). Python program to calculate the area of the square.
# Formula : area = a*a
print("_" *50)
area=2
output=a*a
print("area of the square :",output)

# 16). Python program to calculate the area of a circle.
# Formula = PI*r*r
# r = radius
# PI = 3.14
print("_" *50)
r=2
PI = 3.14
radies = PI*r*r
print("Area of the circle :" ,radies)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
print("_" *50)
a=3
ac=6*a*a
print("Area of the cube :",ac)

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
print("_" *50)
r=4
PI = 3.14
h=4
acy= 2*PI*r*h + 2*PI*r*r
print("Area of the cylinder :",acy)

# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
print("_" *50)
lhs=153
rhs=1*1*1 + 5*5*5 + 3*3*3
print("Armstrong numbers :",lhs,rhs)
print("_" *50)

# 20). Python program to calculate simple interest.
# Formula = P+(P/r)*t
# P = Principle Amount
# r = Anual interest rate
# t = time

p = 100000
r = 10
t = 2
amount = p+(p/r)*t
print("Amount payable: ",amount)
print("_" *50)



