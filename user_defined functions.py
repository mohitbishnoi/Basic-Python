# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:44:10 2019

@author: Mohit
"""

# function us used to perform calculation and return values
# you can create your own functions, all user defined functions
# are present for only one session jsut like variables.

# syntax

# =============================================================================
# def function_name(args):
#     python statement
#     return (var);
# =============================================================================

def add2no(x,y):
    z = x+y
    return (z);

add2no(10,20)
add2no(-20,30)
add2no([10,20],[30])

print(z)

#scope of varaible

# 1. Global variable - variable created outside of a functions
# 2. Local variable - variable created within function, you cannot
# use them outside of a function

z = add2no(10,20)
print(z)

# create a function to find final amount to be paid after 10% discount

# take input as 1000 - result 900

def get_final_amount(price,discount=10):
    amt = price*discount/100
    final_amount = price-amt
    return (final_amount);

get_final_amount(1000)
get_final_amount(1000,20)

