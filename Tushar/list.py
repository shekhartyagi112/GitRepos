mylist=["apple","orange","banana"]
print(mylist)
#['apple', 'orange', 'banana']

mylist=["apple",1,"banana"]
print(mylist)
#['apple', 1, 'banana']
#list accepts diff types of datatypes items

mylist=["apple","banana","orange"]
print(mylist[1])
#banana
#list items can access throgh index

mylist=["apple","banana","orange"]
print(mylist[0:2])
#['apple', 'banana']
#positive index will take value from starting

mylist=["apple","banana","orange"]
print(mylist[-3:-1])
#['apple', 'banana']
#negative index will take value from ending

#check items present in list or not using IN operator
mylist=["apple","banana","orange"]
if "apple" in mylist:
    print('apple is present in list')
else:
    print('apple is not present')
#apple is present in list

#change value in list items using index value
mylist=["banana","orange"]
mylist[0]="apple"
print(mylist)
#['apple', 'orange']

#change range of list items
mylist=["banana","orange","grapes"]
mylist[0:2]=["apple","pineapple"]
print(mylist)
#['apple', 'pineapple', 'grapes']

#append() method used to add list items at the end of list
mylist=["apple","banana","pineapple"]
mylist.append("mango")
print(mylist)
#['apple', 'banana', 'pineapple', 'mango']

#insert() method used to inser list item at specific index

mylist=["apple","banana","orange"]
mylist.insert(0,"grapes")
print(mylist)
#['grapes', 'apple', 'banana', 'orange']

#To append items from another list to current list use extend() method

mylist=["apple","banana","orange"]
mylist1=["pineapple","mango"]
mylist.extend(mylist1)
print(mylist)
#['apple', 'banana', 'orange', 'pineapple', 'mango']
