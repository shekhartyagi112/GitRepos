#integer
"""
a = 5

#float
a=20.5

#complex
c=3j
d=3+4j
"""
#convert int to float

a=4567
"""
b=float(a)
print(b)

#4567.0

b=bool(a)
print(b)

#True

b=complex(a)
print(b)

#(4567+0j)

b=set(a)
print(b)
#'int' object is not iterable

b=list(a)
print(b)
#'int' object is not iterable

b=str(a)
print(b)
#4567
"""

l1 = [1,2,3,4]

l2=tuple(l1)
print(l2)
#(1, 2, 3, 4)

l3=set(l1)
print(l3)
#{1, 2, 3, 4}

#l4=dict(l1)
#print(l4)
#cannot convert dictionary update sequence element #0 to a sequence

l5=bool(l1)
print(l5)
#True


