"""
''' 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
'''
string =  "Shekhar Tyagi"           # "sqatools"
if len(string) < 2:
	print(True)
else:
	last_string = string[:2]+ "_" +string[-2:]
	print(last_string)


# 2). Python string program that takes a list of strings and returns the length of the longest string.
print("2). Python string program that takes a list of strings and returns the length of the longest string.")

string = ["i", "am", "Shekhar", "Tyagi", "123456789"]
temp = 0
for i in string:
	lenth = len(i)        # 1,2,7,5,9
	print(lenth, end=",")
	if lenth > temp:
		temp=lenth          # 1,2,7,9
print("\n",temp)

# 3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
print("3). Python string program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).")

String = "Shekhar Tyagi"
str1 = String[-2: ] * 4
print(str1, end=",")

# 4). Python string program to reverse a string if it’s length is a multiple of 4.
print("4). Python string program to reverse a string if it’s length is a multiple of 4.")

strng = "ShekharTyagi"
if len(strng) % 4 == 0:
	print(len(strng))
	print(strng[::-1])

# 5). Python string program to count occurrences of a substring in a string.
print("5). Python string program to count occurrences of a substring in a string.")

string = "Shekhar Tyagi Shekhar Tyagi Shekhar Tyagi"
sub = "She"
print(string.count("She"))


# 6). Python string program to test whether a passed letter is a vowel or consonant.
print("6). Python string program to test whether a passed letter is a vowel or consonant.")

letter = "shekhartyagi"
for char in letter:
	if char == "a" or char =="e" or char == "i" or char == "o" or char == "u":
		print(f"{char} is vowel")
	else:
		print(f"{char} is consonant")

# 7). Find the longest and smallest word in the input string.
print("7). Find the longest and smallest word in the input string.")

string = "i am shekhar tyagi"
list = string.split(" ")

print("Smallest string: ", min(list, key=len))
print("Smallest string: ", len(min(list, key=len)))
print("longest string: ", max(list,key=len))
print("longest string: ", len(max(list,key=len)))


# 8). Print most simultaneously repeated characters in the input string.
print("8). Print most simultaneously repeated characters in the input string.")

string = "Helllllo ffdfdas sdfsfsd sssfdddd"
max_repeat_count = 0
max_repeat_char = ''
temp =1
for i in range(len(string)-1):
	if string[i] == string[i+1]:
		temp = temp+1
		if temp > max_repeat_count:
			max_repeat_count= temp
			max_repeat_char =string[i]
	else:
		temp=1

print("Max repeated char :", max_repeat_char,
      "\nMax repeated count :", max_repeat_count)


# 9). Write a Python program to calculate the length of a string with loop logic.
print("9). Write a Python program to calculate the length of a string with loop logic.")

string = "i am shekhar tyagi"
count = 0
for char in string:
    count = count+1
print("Length of the string using loop logic: ", count)
print("Length of the string using len(): ", len(string))


# 10). Write a Python program to replace the second occurrence of any char with the special character $.
# Input = “Programming”
print("10). Write a Python program to replace the second occurrence of any char with the special character $.")

str1 = "Programming"
result = ''

for char in str1:
    if char in result:
        result = result + "$"
    else:
        result = result + char

print("Result :", result)

# 11). Write a python program to get to swap the last character of a given string.
# Input = “SqaTool”
print("11). Write a python program to get to swap the last character of a given string.")

string = "SqaTool"
swap_string = string[-1] + string[1:-1] + string[0]
print(swap_string)

# 12). Write a python program to exchange the first and last character of each word from the given string.
# Input = “Its Online Learning”
print("12). Write a python program to exchange the first and last character of each word from the given string.")
'''
string = "Its Online Learning"
exchange_string = string[-16::-1] + string[-9:-17:-1] + string[-1:-9:-1]
print(exchange_string)
'''
# Or

string ="Its Online Learning"
list1 = string.split(" ")
'''
print(list1)        # ['Its', 'Online', 'Learning']
print(list1[-1])    # Learning
print(list1[1:-1])  # ['Online']
print(list1[0])     # Its
'''
for word in list1:
	#print(word, end=" ")   # Its Online Learning
	new_word = word[-1] + word[1:-1] + word[0]
	#print(new_word, end=" ")    #  stI enilnO gninraeL
	index = list1.index(word)
	#print(index, end=" ")    # 0 1 2
	list1[index] = new_word
" ".join(list1)
print(list1)

# 13). Write a python to count vowels from each word in the given string show as dictionary
# Input = “We are Learning Python Codding”
print("13). Write a python to count vowels from each word in the given string show as dictionary")

string= "We are Learning Python Codding"
list1 = string.split(" ")
#print(list1)     # ['We', 'are', 'Learning', 'Python', 'Codding']
vowels = "aeiou"
dictionary = dict()
# print(dictionary)       # {}
for word in list1:
	count = 0
	for char in word:
		if char in vowels:
			count= count+1
			dictionary[word] = count
print(dictionary)

# 14). Write a python to repeat vowels 3 times and consonants 2 times.
# Input = “Sqa Tools Learning”
print("14). Write a python to repeat vowels 3 times and consonants 2 times.")

str1 = "Sqa Tools Learning"
result =""
print(result)
vowels = ["a","e","i","o","u",
		  "A", "E","I","O","U"]
for char in str1:
	if char in vowels:
		result = result+ char*3
	else:
		result= result+char*2
print(result)

# 15). Write a python program to re-arrange the string.
# Input = “Cricket Plays Virat”
print("15). Write a python program to re-arrange the string.")

string = "Cricket Plays Virat"
list = string.split(" ")
list.reverse()
" ".join(list)
print(list)

# 16). Write a python program to get all the digits from the given string.
Input = '''
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
'''

print("16). Write a python program to get all the digits from the given string.")
string = '''Sinak’s 1112 aim is to 1773 create a new generation of people who 
 understand 444 that an organization’s 5324 success or failure is 
 based on 555 leadership excellence and not managerial acumen '''
list1 = string.split(" ")
list2 = [ ]
for val in list1:
	if val.isdigit():
		list2.append(val)
print(list2)

# 17). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = “JAVA is the Best Programming Language in the Market”
print("17). Write a python program to replace the words “Java” with “Python” in the given string.")

string = "Java is the Best Programming Language in the Market."
list1 = string.split(" ")
for val in list1:
	#print(val, end=" ")
	if val == "Java":
		index = list1.index(val)
		list1[index] = "Python"
print(" ".join(list1))

# 18). Write a Python program to get all the palindrome words from the string.
# Input = “Python efe language aakaa hellolleh”
print(" 18). Write a Python program to get all the palindrome words from the string.")

string = "Python efe language aakaa hellolleh"
list1 = string.split(" ")
list2 = [ ]
for val in list1:
	if val == val[::-1]:
		list2.append(val)
print(list2)


# 19). Write a Python program to create a string with a given list of words.
# Input = [“There”, “are”, “Many”, “Programming”, “Language”]
print("19). Write a Python program to create a string with a given list of words.")

list1= ["There", "are", "Many", "Programming", "Language"]
list2 = " ".join(list1)
print(list2)

# 20). Write a Python program to remove duplicate words from the string.
# Input = “John jany sabi row john sabi”
print("20). Write a Python program to remove duplicate words from the string.")

string = "John jany sabi row John sabi"
list = string.split(" ")
list2 = [ ]
for val in list:
	if val not in list2:
		list2.append(val)
print(" ".join(list2))


# 21). Write a Python to remove unwanted characters from the given string.
# Input = “Prog^ra*m#ming”
print("21). Write a Python to remove unwanted characters from the given string.")

string = "Prog^ra*m#ming"
test_str= [ ]
for latter in string:
	if latter.isalnum():
		test_str.append(latter)
print("".join(test_str))
print()

string1 ="Py(th)#@&on Pro$*#gram"
test_str= [ ]
for latter in string1:
	if latter.isalnum():
		test_str.append(latter)
print("".join(test_str))
"""

# 22). Write a Python program to find the longest capital letter word from the string.
# Input = “Learning PYTHON programming is FUN”
# Output = “PYTHON”
print("22). Write a Python program to find the longest capital letter word from the string.")

str1 = "Learning PYTHON programming is FUN "
long_word = ''
max_len = 0

word_list = str1.split()

for word in word_list:
    word_len = len(word)
    if word_len > max_len and word.isupper():
        max_len = word_len
        long_word = word
print("long word capital word :", long_word)





