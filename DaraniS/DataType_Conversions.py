#***************************************int****************************************


#convert int to float
var1 = 12
var2 = 3.56
var3 = float(var1)+var2

print("convert int to float", type(var3), var3)

#convert int to string
int1 = 123
int2 = "456"
int3 = str(int1)+int2
print("convert int to string", type(int3), int3)

#cannot convert int to list
#cannot convert int to Dict
#cannot convert int to set
#cannot convert int to tuple
#convert int to Boolean
int1 = 123
int2 = bool(int1)
print("convert int to Boolean", type(int2), int2)

#*******************************Float*************************************

#convert float to int

var1 = 12
var2 = 3.56
var3 = float(var1) - var2

print("convert float to int", type(var3), var3)

#convert float to string

flo1 = 123.57
flo2 = "456"
flo3 = flo1 + float(flo2)
print("convert float to string", type(flo3), flo3)


#cannot convert Float to list
#cannot convert Float to Dict
#cannot convert Float to set
#cannot convert Float to tuple
#convert Float to Boolean
flo1 = 123
flo2 = bool(flo1)
print("convert Float to Boolean", type(flo2), flo2)


#*************************************string*********************************

#Convert String to int
#when we have only numbers in the string then the conversion is possible to int and float

str1 = "123"
str3 = int(str1)
print("Convert String to int", type(str3), str3)

#Convert String to Float
str1 = "123.23"
str3 = float(str1)
print("Convert String to Float", type(str3), str3)

#Convert String to list
str1 = "DaraniSunkara"
str2 = list(str1)
print("Convert String to list", type(str2), str2, " , Index of 0-5 : ", str2[0:5])

#Convert String to set
str3 = "Python Programming"
str4 = set(str3)
print("Convert String to set", type(str4), str4)

#convert String to Dict
#only possible if the string is in the form of Json Structure and string data should be in the single quotes
import json
str5 = '{"Name" : "Darani Sunkara" , "Age" : 25}'
data = json.loads(str5)
print("Convert String to dict", type(data), data)

#convert string to Boolean
str6 = "darani"
str7 = bool(str6)
print("convert string to Boolean", type(str7), str7)

