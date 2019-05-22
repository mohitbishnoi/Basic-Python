# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:18:09 2019

@author: Mohit
"""

#Topic = List

# =============================================================================
# list- it is used to store multiple values of same type or different type
# list store values in a sequance, where sequance starts from zero
# =============================================================================

list1 = [10,20,30]
list2 = ['a','b','c']
list3 = ['a',10,'b',20,'c',30]

list1;list2;list3
# ;= is used to give multiple statement in a single line
print(list1,list2,list3)

# =============================================================================
# list() - will not create list
# =============================================================================
# =============================================================================
# list{} - will  not create list
# =============================================================================

# data extraction from list
list1[0] # - display first value stored in list

list1[-1] # - diaplay last value from the list

len(list1) # - return number of value stored in list

type(list1) # - return data type of given variable

#to display multiple values or to extract multiple values from list

#list slicing - start:stop - here start will be included and stop will be excluded

list1[1:3] # - first and second position values

list1[1:] # - from 1 to last position value
list1[:1] # - from 0 to 0
list1[:] # - all values

# =============================================================================
# # do following task with respect to list3
# =============================================================================

#1. extract values from 1 to 4
#2. extract 5th values
#3. extract second last value
#4 extract all values except first

list3[1:5]

list3[4]

list3[-2]

list3[1:]


#create a list called price with below given data
#mon 100 tue 120 wed 140 thu 150 fri 180

#find fri price
# extract values from 1 to 4

Price = [['mon',100],['tue',120],['wed',140],['thu',160],['fri',180]]

Price[-1][1]

Price[1:5]


# =============================================================================
# #List Manupulation
# adding new values
# removing values
# replacing values
# sort values
# reverse values
# =============================================================================
list1.append(40)
list1

#insert 15 between 10 and 20

list1.insert(1,15)
list1

#remove 30
list1.remove(30)

list1

#replace 20 to 25
list1[2]=25
list1

#sort  values
list1.sort()

# reverse values
list1.sort(reverse = True) #decending order sorting


list1.reverse()

list1




























