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
#### Integer #####

num1 = 40

# int -> float
var1 = float(num1)
print(var1, type(var1))
# 40.0 <class 'float'>

# int -> string
num2 = 5678
var2 = str(num2)
print(var2, type(var2), var2[2])
# 5678 <class 'str'> 7

# int -> list # conversion is not possible
"""
num3 = 67546756
var3 = list(num3)
print(var3)
"""

# int -> tuple # conversion is not possible
# int -> dict  # conversion is not possible
# int -> set   # # conversion is not possible
"""
num4 = 600
var4 = set(num4)
print(var4, type(var4))
"""
# Int -> Boolean
num5 = 10
var5 = bool(num5)
print(var5, type(var5))
# True <class 'bool'>

num6 = 0
var6 = bool(num6)
print(var6, type(var6))
# False <class 'bool'>


###################### Float ################
print("_"*50)

# float -> int
num1 = 55.67
var1 = int(num1)
print(var1, type(var1))
# 55 <class 'int'>

# float -> string
num2 = 67.88
var2 = str(num2)
print(var2, type(var2), var2[3])
# 67.88 <class 'str'> 8

# float -> list : conversion is not possible
# float -> tuple : conversion is not possible
# float -> dict : conversion is not possible
# float -> set : conversion is not possible

# float -> boolean
num3 = 77.34
var3 = bool(num3)
print(var3, type(var3))
# True <class 'bool'>

num4 = 0.0
var4 = bool(num4)
print(var4) # False

######## String ########
print("_"*50)
# string -> int
"""
str1 = "Hello"
var1 = int(str1)
print(var1)
# ValueError: invalid literal for int() with base 10: 'Hello'
"""

# If string contains only number, then string to int conversion is possible
str2 = "6546799"
var2 = int(str2)
print(var2, type(var2), var2*2)
# 6546799 <class 'int'> 13093598

### string -> float

str3 = "good morning"
# var3 = float(str3)# conversion is not possible

str4 = "55.78"
var4 = float(str4)
print(var4, type(var4))
# 55.78 <class 'float'>


# string -> list
stra = "Python"
list1 = list(stra)
print(list1, type(list1))
print(list1[2])
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>
# t


# string -> tuple
strb = "Programming 56456"
tup1 = tuple(strb)
print(tup1, type(tup1))
print(tup1[0])
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', ' ', '5', '6', '4', '5', '6') <class 'tuple'>
# P


# string -> dict
"""
strc= "Good Morning"
dict1 = dict(strc)
print(dict1, type(dict1))
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
"""
import json

strf = '{"Name" : "John", "age" : 25, "mobile": 876865788}'
#strf = "{'Name' : 'John', 'age' : 25, 'mobile': 876865788}"
print(strf, type(strf))
# {"Name" : "John", "age" : 25, "mobile": 876865788} <class 'str'>
data = json.loads(strf)
print(data, type(data))
print(data['mobile'])
# {'Name': 'John', 'age': 25, 'mobile': 876865788} <class 'dict'>


# string -> set
strg = "Hello"
set1 = set(strg)
print(set1, type(set1))
# {'e', 'o', 'l', 'H'} <class 'set'>



# string -> Boolean

strh = "Good"
bol1 = bool(strh)
print(bol1, type(bol1))
# True <class 'bool'>

strj = ""
bol2 = bool(strj)
print(bol2, type(bol2))
# False <class 'bool'>
























































