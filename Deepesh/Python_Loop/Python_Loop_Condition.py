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

