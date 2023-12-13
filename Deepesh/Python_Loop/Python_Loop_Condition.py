# range(10)
"""
for i in range(10):
    print(i)
"""
# range method with default initial value is zero
# and difference value is 1
for i in range(11):
    print(i)

print("_"*40)
# initial value is 1 and last value is 10 and difference is 1
for var in range(1, 10):
    print(var)

# initial value 1
# end value 10
# difference value is 2
print("_"*40)
for i in range(1, 10, 2):
    print(i)

print("_"*50)
# program to print all the even number from 1 to 20
for i in range(1, 20):
    if i%2 == 0:
        print(i)


# print table of any given number
num = 7

for i in range(1, 11):
    print(num,"*",i, ":", i*num)


# write a program to find out all the number which are divible by 3
# between 1 to 50

###################################
# write a program to calculate the factorials of any given number
print("_"*40)
# 5 = 5 * 4 * 3 * 2 * 1
num = 4
fact = 1
for i in range(num, 0, -1):
    print(i)
    fact = fact*i
    # i=  6, fact = 6*1 : 6
    # i = 5, fact = fact*i = 6*5 : 30
    # i = 4, fact = 30*4 = 120
    print("fact :", fact)

# write a program to print the fabonaci series
print("_"*50)
# a  b  a   b
# 0, 1, 1,  2, 3, 5, 8, 13, 21 ...
#    a  b  a+b
# a = b
# b = a+b
a = 0
b = 1
for _ in range(10):
    print(b, end=" ")
    a, b = b,  a+b # 1, 1+0 | a=1,  b=1
                   # 1, 1+1  | a =1, b=2
# 1 1 2 3 5 8 13 21 34 55

print()
# write a python program to find out the given number is prime or not
# prime number : the which can divide by 1 or the number itself.
# prime number : 1, 2, 3, 5, 7, 11, 13, 17, 19, 23 ...
print("_"*50)
num1 = 23
prime = True
for i in range(2, num1//2):
    # i = 2, num1 = 10 : 10%2 == 0
    # i = 3, num1 = 11 : 11%3 == 0
    print("i :", i)
    if num1%i == 0: #
        prime = False
        break


if prime:
    print("this is prime number :", num1)
else:
    print("this is not a prime number :", num1)




# Program to find out the factorial of any number.
"""
print("_"*50)
numa = int(input("Please enter number to get factorial :"))
#factorial: 4*3*2*1 : 24
result = 1

for i in range(numa, 0, -1):
    print(i)
    result = result*i
    # result = 1, i = 4
    # 1*4 = 4 | result = 4,
    # result = 4, i = 3 | 4*3 = 12

print("factorial output :", result)

# print("_"*40)
# for i in range(10, 1, -1):
#     print(i)
"""


# python program to get the sum all the numbers from 1 to 10
summation = 0
for i in range(1, 11):
    summation = summation + i

print("sum values :", summation)
print("sum values :", summation)


#############################################
#apply loop on list data
print("_"*40)
even_sum = 0
odd_sum = 0
list1 = [4, 6, 7, 23]

for val in range(1, 21):
    if val%2 == 0:
        even_sum = even_sum + val
    else:
        odd_sum = odd_sum + val

print("even sum :", even_sum)
print("odd sum :", odd_sum)



# add even and odd numbers from 1 to 20
print("_"*40)
even_sum = 0
odd_sum = 0

for val in range(1, 21):
    if val % 2 == 0:
        even_sum = even_sum + val
    else:
        odd_sum = odd_sum + val

    print("val :", val)
    print("even sum :", even_sum)
    print("odd sum :", odd_sum)
    print("_"*5)





























