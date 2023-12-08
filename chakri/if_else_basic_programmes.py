#1). Python program to check given number is divided by 3 or not.

'''N = int(input('enter any number : ') )
if N%3 == 0:
    print(N , ' can be divided with 3')
else:
    print(N , 'can not be divide with 3')


#2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1,30):
    if i%3 == 0:
        print(i,end = " ")

print('-'*40)
#3), If else program to get all the numbers divided by 9 from 1 to 30.

for i in range(1,30):
    if i%9 == 0:
        print(i,end= " ")

print('-'*50)

3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
m = int(input('enter student marks : '))
if m < 40:
    print('failed')
elif m>=40 and  m<=50:
    print('grade c')
elif m>50 and  m<=60:
    print('grde B')
elif m>60 and  m<=70:
    print('grade A')
elif m>70 and  m<=80:
    print('grade A+')
elif m>80 and  m<=90:
    print('grade A++')
elif m>90 and  m<=100:
    print('good excelent')
else:
    print('invalid marks')
######################################################################
#4). Python program to check the given number divided by 3 and 5.
n = int(input('enter any number : '))
if n%3 == 0:
    print(n, 'can divided with 3')
else:
     print(n,'can not be divide with 3')
if n%5 == 0:
        print(n,'can divided with 5')
else:
        print(n,'can divided with 5')

#5). Python program to print the square of the number if it is divided by 11.

a = int(input('enter any number : '))
if a%11 == 0:
    print(a**2)
else:
    print(a,' can not divided by 11 ')

#7). Python program to check given number is odd or even.

e = int(input('enter any number to know given number is even or not :'))
if e%2 == 0:
    print('given nuber is even number')
else:
    print('given number is odd number')

#9). Python program to check authentication with the given username and password.

user = 'chakri'
password = 'chakri@180'
u = input('enetr user name:')
p = input('enter passwod : ')
if u == user and password == p:
    print('logged in successfully')
else:
    print('incoreect credentials')



#10). Python program to validate user_id in the list of user_ids.

ls1 = ['chakri','siragam','9154',350]
n = input('enter user id : ')
if n in ls1:
    print('user id is valid')
else:
    print('user id not valid')

#11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

n = int(input('enter any nuber : '))
if n%2 == 0:
    print(n,'square' ,n**2)
else:
    print('given number cant divided by 2')
if n%3 == 0:
    print(n ,'qube ',n**3)
else:
    print('given number cant be diveded by 3')

#12). Python program to describe the interview process.

r1 = input('enter round 1 result (passed or failed):')
r2 = input('eneter round 2 result (passed or failed) :')
if r1 == 'passed':
    print('round 1 passed get ready for round 2 ')
    if r2 == 'passed':
        print('passed in round 2 and you are placed ')
    else:
        print('sorry you are failed round 2 better luck next time')
else:
    print('sorry you are failed round 1 better luck next time')
    '''

