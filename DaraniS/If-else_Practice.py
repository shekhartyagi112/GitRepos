#1). Python program to check given number is divided by 3 or not.

num1 = int(input("Enter the number :"))
if num1%3 == 0:
    print("The given number is divided by 3")
else:
    print("The given number is  not divided by 3")

#2). If else program to get all the numbers divided by 3 from 1 to 30.

for i in range(1,31):
    if i%3 == 0:
        print(i)

#3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks


marks = int(input("Enter the marks :"))
if marks<40 :
    print("Your are failed")
elif marks>=40 and marks<=50:
    print("Your grade is : C")
elif marks>50 and marks<=60:
    print("Your grade is : B")
elif marks>60 and marks<=70:
    print("Your grade is : A")
elif marks>70 and marks<=80:
    print("Your grade is : A+")
elif marks>80 and marks<=90:
    print("Your grade is : A++")
elif marks>90 and marks<=100:
    print("Your grade is : Excellent")
else:
    print("Invalid marks")
#Python program to check the given number divided by 3 and 5.
num1 = int(input("Enter the number :"))
if num1%3 == 0 and num1%5 == 0:
    print("The given number is divided by 3 and 5")
else:
    print("The given number is  not divided by 3 and 5")


#5). Python program to print the square of the number if it is divided by 11.
num4 = int(input("enter the number"))
square = num4**2
if num4%11==0:
    print("the given square of the number which is divided  by 11",square)
else:
    print("the given square of the number is not divided  by 11")

#6). Python program to check given number is odd or even.
num5 = int(input("enter the number"))
if num5%2==0 :
    print("the given number is even number")
else:
    print("the given number is odd number")

#7). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num6 = int(input("enter the number"))
if num6%2==0:
    print(num6**2,"Square")
elif num6%3==0:
    print(num6**3,"Cube")
#8). Python program to find the largest number among three numbers.
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))

if num1>num2 and num1>num3:
    print(f"{num1} num1 is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} num2 is greater")
elif num3>num1 and num3>num2:
    print(f"{num3} num3 is greater")

