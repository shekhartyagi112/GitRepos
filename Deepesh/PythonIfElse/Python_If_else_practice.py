"""
if  condition:
    code
else:
    code
"""
"""
num1 = 50
num2 = 51
print(num1 == num2)
if num1 == num2:
    print("both numbers are equal", num1, num2)
else:
    print("both numbers are not equal", num1, num2)


user_input = input("Please enter the value :")
user_input = int(user_input)
print(user_input, type(user_input), user_input*2)
"""
"""
print(user_input%2 == 0)
if user_input%2 == 0:
    print("This is even number :", user_input)
else:
    print("This is odd number :", user_input)
"""

"""
> : greater than
>= : greater than equal to
< : less than
<= : less than equal to
!= : not equal
== : equal to

Logical operator and , or
cond1 and cond2 
True and False : False
False and True : False
True and True : True
False and False : False

cond1 or cond2

True or False : True
False or True : True
True or True : True
False or False : False
"""

#
print("_"*40)
a = 80
b = 100
c = 40


#   True and True : True
#   True and False : False
#   False and False : False
#   False and True : False
"""
if a > b and a > c:
    print("and cond :a has greater value")
else:
    print("and cond : a does not have greater value")


#  False or True : True
if a > b or a > c:
    print("or cond : a has greater value")
else:
    print("or cond : a does not have greater value")
"""

"""
# program : check any number is divisible by 3 and 7
num1 = int(input("Please enter the number :"))
if num1%3 == 0 and num1%7 == 0:
    print("Given number can be divide by 3 and 7 :", num1)
else:
    print("Given number can not be divide by 3 and 7 :", num1)
"""

######### If- elif condition check #########
"""
if cond1:
    code
elif cond2:
    code
elif cond3:
    code
else:
    code
"""

"""
# program : write a program to print student grade as per marks percentage
marks = int(input("Enter students marks :"))


if marks >= 30 and marks <= 40:
    print("student passed with 3rd grade")
elif marks > 80 and marks <= 100:
    print("student passed with A++ grade")
elif marks >= 40 and marks <= 50:
    print("student passed with 2nd grade")
elif marks > 50 and marks <= 65:
    print("student passed with 1st grade")
elif marks > 65 and marks <= 80:
    print("student passed with A+ grade")
elif marks < 30:
    print("Really sorry you are failed")
else:
    print("Marks can not more than 100")
"""
"""
Nested if condition

if cond1:
     code
     if cond2:
        code
     else:
         code
else:
     code
"""

round1 = "pass"
round2 = "fail"

if round1 == "pass":
    print("first round is cleared")
    if round2 == "pass":
        print("second round is cleared !!")
    else:
        print("second round is not clear, please try next")
else:
    print("first round is  not clear,  try next time")

