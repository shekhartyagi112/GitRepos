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
print("#Integer")
print('_'*7)
int1 = 200
print(int1)
# int -> float
print("#Int-->float")
print('_'*12)
Var = float(int1)
print(Var, "\n", type(Var))

# int -->string
print("#int --> string")
print('_'*15)
int = 500
string = str(int)
print(string, "\n" , type(string))


# int -> list # conversion is not possible
"""
int = 12345
lis = list(int)
print(lis, "\n", lis)

"""

# int -> tuple # conversion is not possible
# int -> dict  # conversion is not possible
# int -> set   # # conversion is not possible
"""
num = 12345
set1 = set(num)
print(set1, "\n", set1)

"""

# Int -> Boolean
print("#Int -> Boolean")