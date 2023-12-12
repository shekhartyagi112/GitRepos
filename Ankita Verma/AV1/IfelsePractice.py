#Ifelse condition
#Number is divided by 3 or not

'''num = input("Please enter number:")
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("number is not divisible by 3")'''




"""Print number divide bye 3"""


"""for i in range(1,51):
    if i%3==0:
        print(i, "Number is divisible by 3")"""

 ##If else program to get all the numbers divided by 5 from 1 to 30.

"""for i in range(1,31):
    if i%5 ==0:
        print("Number is divisible",i)"""


#f else program to assign grades as per total marks.
"""marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks"""


user_Input = int(input("Enter Grades "))
if user_Input<40:
    print("Fail")
elif user_Input>=40 and user_Input<=50:
    print( "Grade C")
elif user_Input>=50 and user_Input<=60:
    print("Grade B")
elif user_Input>=60 and user_Input<=70:
    print("Grade A")
elif user_Input>=70 and user_Input<=80:
     print("grade A+")
elif user_Input>=80 and user_Input<=90:
     print(" A++")
elif user_Input<= 100:
     print(" Excellent")
elif user_Input>100:
     print(" Invalid marks")
