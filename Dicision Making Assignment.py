# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:56:25 2019

@author: Mohit
"""
# 1.	Find the sum of all the numbers stored in a list.
new_list = [1,2,3,4,5]
sum(new_list)

# 2.	Check if a number is positive, negative or zero.
num=5
if (num>0):
    print("postive")
elif(num<0):
    print("negitive")
else:
    print("zero")

# 3.	Check greatest number among three numbers.  
max=new_list[0]    
for i in range(1,len(new_list)):
    
    if (max<new_list[i]):
        max=new_list[i]
print(max)

