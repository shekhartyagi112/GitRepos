#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''Input1:1500
Input2:2700
for i in range(1500,2701):
        if i%7 == 0 and i%5 == 0:
            print(i, end=" ")

#3). Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]
print(str1)

#4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for val in numbers:
    if val%2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)


#5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
for i in range(0,6):
    if i != 3 and i != 3:
     print(i)

#7). Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz”.
for i in range(1,31):
    if i%3 == 0 and i%5 == 0 :
        print('fizzbuzz')
    elif i%3 == 0 :
        print('fizz')
    elif i%5 == 0 :
        print('buzz')


for i in range(6):
    print(i*'*')
for i in range(4,0,-1):
    print(i*'*')

num = 2
fact = 1
for i in range(num, 7, 1):
    fact = fact*i
    print("fact :", fact)


a = 0
b = 1
for _ in range(10):
    print(b, end=" ")
    a ,b = b,a+b

even = 0
odd = 0
for i in range(1,10):
    if i%2 == 0:
        even = even+i
    else:
        odd = odd+i
print('sum of even numbers:',even)
print('sum of odd number:',odd)
'''












