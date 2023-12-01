#1). Python Program to add two integer values.

x= 10
y= 20
z=x+y
print(z)

#2). Python Program to subtract two integer values.

x=20
y=10
z=x-y

print(z)

#3). Python program to multiply two numbers.

Val1 = 20
Val2 = 30
Mult = Val1*Val2

print(Mult)

#4). Python program to repeat a given string 5 times.

inp = "we are togather, "

print(inp * 5)

#5). Python program to get the Average of given numbers.

a = 40
b = 50
c = 30

Avg = (a+b+c)/3
print("Avarage:" ,Avg)

#6). Python program to get the median of given numbers. Note: (Doubts)

L1 = [45, 60, 61, 66, 70, 77,80]       #List
x = L1.sort()      # It is using for sort the list in ascending order and return None.
y = (len(L1))      # It is using for return the number of items in a container (List).
z = y/2
print(y)
print(z)
print("Median :",L1[int(z)])

#8). Python program to interchange values between variables.

a = input("enter the value1 : ")
b = input("enter the value2 : ")
a,b = b,a
print("a:",a)
print("b:",b)

#9). Python program to solve this Pythagorous theorem.

import math
s1 = 3
s2 = 5
hypo = (s1**2 + s2**2)
print("hypotenuse side :" ,math.sqrt(hypo))
