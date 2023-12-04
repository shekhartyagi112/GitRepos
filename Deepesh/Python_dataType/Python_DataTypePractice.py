#
"""
var1 = 400
print(type(var1))

var2= "Good Morning"
print(var2, type(var2))
"""
# Python Data Type
"""
1.  Numbers
    a).  Integer
    b).  Float
    c). Complex Number
    
2.  Sequencial data type
    d). String
    e). Tuple
    f). List
    
3. Dictionary 

4. Set

5. Boolean 
"""

# Integer (int)
"""
num1 = 200
num2 = 435435435445346456
num3 = 0

print(type(num1), type(num2), type(num3))
"""

num2 = 56645645645
num4 = num2*2
print(num4, type(num4))

num5 = 200*44.23
print(num5, type(num5))

var2 = "Good morning"
print(var2, type(var2))

"""
Int properties:

1.  Int is immutable data type
2.  There is no limit to set value for int datatype.
"""

######### Float Data Type ###########

var11 = 55.34
var22= 0.0034
var33 = 4.56344454454545454545454545454

print(var11, type(var11))
print(var22, type(var22))
print(var33, type(var33))

"""
Int properties:

1.  Int is immutable data type
2.  There is no limit to set value for float datatype.
"""

############# Complex number ###########
print("_"*50)
varp = 50 + 40j
print(varp, type(varp))
# (50+40j) <class 'complex'>


############ String #################
print("_"*50)

str1 = "Hello"
str2 = 'Good morning'
str3 = """Hello Good morning
Hope you are doing good
Happy Learning
"""

str4 = '''Lets have part today
Its very easy to learn programming'''

str5 = "India won the 't20' series"
str6 = 'Have a "nice" day'

print(str1,  type(str1))
print(str2,  type(str2))
print(str3,  type(str3))
print(str4,  type(str4))
print(str5,  type(str5))
print(str6,  type(str6))

print("_"*40)
# +ve    0   1  2   3  4
# strx ="H   e  l   l  o"
# -ve   -5  -4 -3  -2 -1
strx = "Hello"
print(strx[2])
print(strx[0])
print(strx[-4])

"""
String is also a immutable data type
"""

################# list ###################
print("_"*50)

#        0   1   2     3
list1 = [5, 2.5, 55, 'Hello']
#       -4  -3   -2   -1

print(list1, type(list1))

# list1[1] = "Good morning"
# print(list1)

# var1 = "Python Programming"
# var1[0] = "K"
# print(var1)
print(list1[1], list1[-3])

list1 = [40, [4, 7, 8], (4, 6), 'Hello', {'a': 30, 'b' : 40}, {5, 7, 8}]
print(list1)

"""
Properties:
-> List is mutable data type
-> Any type of data can be member of list
-> List follows the positive and negative indexing as like string
"""

################## Tuple ################
print("_"*40)

tup1 = (5, 7, 2, 8, 'Hello', [4, 6, 7], (33, 55, 77))
print(type(tup1), tup1)

print(tup1[0])  # 5
print(tup1[-1])  # (33, 55, 77)

"""
Properties:
-> Tuple is immutable data type
-> Any type of data can be member of tuple
-> Tuple follows the positive and negative indexing as like string
"""

tup2 = (4, 7, 9, 2)
tup2[1] = 100

print(tup2)

"""
tup2[7] = 100
    ~~~~^^^
IndexError: list assignment index out of range
"""