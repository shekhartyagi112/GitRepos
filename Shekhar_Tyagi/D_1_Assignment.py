#1). Python Program to add two integer values.
print("1). Python Program to add two integer values.")

x= 10
y= 20
z=x+y
print(z)

#2). Python Program to subtract two integer values.
print("2). Python Program to subtract two integer values.")

x=20
y=10
z=x-y

print(z)

#3). Python program to multiply two numbers.
print("3). Python program to multiply two numbers.")

Val1 = 20
Val2 = 30
Mult = Val1*Val2

print(Mult)

#4). Python program to repeat a given string 5 times.
print("4). Python program to repeat a given string 5 times.")

inp = "we are togather, "

print(inp * 5)

#5). Python program to get the Average of given numbers.
print("5). Python program to get the Average of given numbers.")

a = 40
b = 50
c = 30

Avg = (a+b+c)/3
print("Avarage:" ,Avg)

#6). Python program to get the median of given numbers. Note: (Doubts)
print("6). Python program to get the median of given numbers. Note: (Doubts)")

L1 = [45, 60, 61, 66, 70, 77,80]       #List
x = L1.sort()      # It is using for sort the list in ascending order and return None.
y = (len(L1))      # It is using for return the number of items in a container (List).
z = y/2
print(y)
print(z)
print("Median :",L1[int(z)])

#7). Python program to print the square and cube of a given number.
print("7). Python program to print the square and cube of a given number.")

s1 = 8
R1 = 8**2  # Num**2 is for square
R2 = 8**3  # Num**3 is for cube
print("sq:",R1)
print("Cube:", R2)

#8). Python program to interchange values between variables.
print("8). Python program to interchange values between variables.")

a =  200      #input("enter the value1 : ")
b =  300      #input("enter the value2 : ")
a,b = b,a
print("a:",a)
print("b:",b)

#9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
print("9). Python program to solve this Pythagorous theorem.")

import math
s1 = 3
s2 = 5
hypo = (s1**2 + s2**2)
print("hypotenuse side :" ,math.sqrt(hypo))

#10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
print("10). Python program to solve the given math formula.")

a = 5
b = 4
#R1 = a**2 + b**2 + 2*a*b
R1 = 5**2 + 4**2 + 2*5*4

#R2 = (a+b)**2
R2 = (5+4)**2
print("(a+b)^2 :", R1)
print("(a+b)^2 :", R2)

#11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
print("11). Python program to solve the given math formula.")

a = 8
b = 3

#R1 = a^2 + b^2 – 2ab
R1 = 8**2 + 3**2 - 2*8*3

#R2 = (a-b)^2
R2 = (8-3)**2

print("(a-b)^2 :", R1)
print("(a-b)^2 :", R2)

#12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
print("12). Python program to solve the given math formula.")

a = 5
b = 3

#R1 = (a-b)*(a+b)
R1 = (5-3)*(5+3)
#R2 = a^2-b^2
R2 = 5**2-3**2
print("(a^2-b^2):",R1)
print("(a^2-b^2):",R2)

# #13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3

