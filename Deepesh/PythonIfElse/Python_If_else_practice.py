"""
if  condition:
    code
else:
    code
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
print(user_input%2 == 0)
if user_input%2 == 0:
    print("This is even number :", user_input)
else:
    print("This is odd number :", user_input)
"""