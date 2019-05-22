# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:48:09 2019

@author: Mohit
"""

#datatype = different type od values python can store
#1 integer - numeric values
#2  float - numeric values with decimal
#3 string - character or any types of value
#4 complax - a+bj where 'a' is real value and 'b' is imaginary values

#placeholder
#1 list
#2 tuple
#3 dictionary


x = 10
y = 10.0
#type() - return data types of a variable
type(x)
#bool - boolean value - it is a subtype of integer
z = True
type(z)


student_id = 'A101'

com = 1+2j
type(com)

a = 1+2j
b = 2+3j

c=a+b #3+5j
d = a*b #2*(1+2j)+3j*(1+2j) = 2+4j+3j+6 = -4+7j

print(c,d)

b1=True #1
b2=False  #0

b1+b2
b1*b2
b1&b2 #b1 and b2
b1|b2 #pipeline - b1 or b2 


learn = "python"
learn = learn.upper()

learn
len(learn)

new = learn+" learning" #concatination
new

#Python learning
newr = new[0]+new[1:6].lower()+' '+new[7].upper()+new[8:]
print(newr)

#pyTon
learn[0:2].lower()+learn[2].upper()+learn[4:6].lower()

#list slicing
listname[start:stop] - #extract value from start and stop position excluding stop position




