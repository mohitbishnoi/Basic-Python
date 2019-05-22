# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:06:19 2019

@author: Mohit
"""

#Create a list with the name Newlist that will contain the following values –
#Rakesh, 18.9, 23, Mahesh, 356, 26.8

Newlist = ['Rakesh',18.9,23,'Mahesh',365,26.8]
Newlist


#Create a nested list with the name PersonDetails and values –
#Mike, (1984, 2017), Jay, (1979, 2017)

PersonDetails = ['Mike',(1984,2017),'Jay',(1979,2017)]
PersonDetails

#Access the following values of the corresponding lists –
#i. 3rd value of Newlist.
Newlist[2]
#ii. 4th value’s 2nd element of PersonDetails list.
PersonDetails[3][1]
#iii. 2nd value from the last of Newlist
Newlist[-2]

#4. Create a list my_list containing all the alphabets of ILOVEPYTHON as individual element. And perform the following task:
my_list = ['i','l','o','v','e','p','y','t','h','o','n']
#i. access the elements 3rd to 5th
my_list[2:5]
#ii. access the elements beginning to 4th
my_list[3:]
#iii. access the elements 6th to end
my_list[5:]
#iv. access the elements beginning to end
my_list[:]
#v. Repeat the list 4 times and save it with a name my_newlist and find the length of my_newlist
my_newlist = my_list*4
len(my_newlist)
#vi. Find the position of “P” in my_list.
my_list.index("p")

#Create a list evenno containing the values (2,4,7,8,10) and oddno containing the value (1,2,4,6,9) and perform the following task:
evenno = [2,3,7,8,10]
oddno = [1,2,4,6,9]
#i. change the 3rd item of evenno to 6
evenno[2]=6
#ii. change 2nd to 4th elements of oddno to (3,5,7)
oddno[1:4]=[3,6,7]
#iii. add both the list
evenno+oddno
#iv. Remove 2nd to 4th element in the list evenno
del evenno[1:4]
#v. Insert the value (12,14,16) into evenno list
evenno.extend([12,14,16])