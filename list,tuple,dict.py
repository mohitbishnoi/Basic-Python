# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 09:56:43 2019

@author: Mohit
"""

#list - list is used to store multiple values,values can be of same type and different type
# we use square brecket[] to create list.

mylist = ['a',10,'b',20,'c',30]
type(mylist)

#tuple - is used to multiple values, values can be same type or differnet type. we use small() brecket 
# to create tuple. tuple is immutable.

mytuple = ('a',10,'b',20,'c',30)
type(mytuple)

#Dictionary - is used to store multiple values on key-pair
#here key is unique, and values can be any value.
# we use {} to create dictionary.

mydict = {'a':10,'b':20,'c':30}

type(mydict)

#change 20 to 25 in all objects

mylist[3]=25  
mylist

mytuple[3]=25 #not working, you can not change values in tuple

mydict['b']
mydict.keys()
mydict.values()

mydict['b'] = 25

mydict


#adding new values in object, 'd',50

mylist = mylist+['d',50]
mylist

mytuple = mytuple+('d',50)
mytuple

mydict['d']=50
mydict

#remove values from object - delete 30 from object
del mylist[5]
mylist
mylist.remove('c')
mylist

del mytuple(5) #not working, you can not change values in tuple

mydict.pop('c')
mydict
