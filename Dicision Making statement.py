# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:26:14 2019

@author: Mohit
"""

# =============================================================================
# #Topic : Dicision making statements
# =============================================================================

#any statement or calculation 


# =============================================================================
# #if(condition)
# #    action
# =============================================================================
if(True): print("good")

time=12
if (time<12):
    print("good morning")
print("good day")
# =============================================================================
# 
# # if (condition):
# #   action1
# #else:
#     #action2
# #action will work if condition is true else condition
# =============================================================================

# find square root of x if x is less then 10, else
#find square root of x

x = int(input("enter x: "))
if (x<10):
    print(x**0.5)
else:
    print(x*x)
    
    
# =============================================================================
# if(condirion 1):
#     action1
# elif(condition 2):
#     action2
# else:
#     action 3
# =============================================================================
    
#write python code to calculate square of user given value
#if value is below 10, and find square root if value is
#below 20, else increment value by 10

    
user_value = int(input("Enter any value: "))
if (user_value<10):
    new_value=user_value*user_value
    print(new_value)
elif(user_value<20):
    print(user_value**0.5)
else:
    print(user_value+10)
    
# Case - 1 - write python code to find total to be paid by 
    # customer if there is offer of buy1 - 30% discount and
    # buy 2 - 50% discount
    
def get_finalAmt(price,qty):
    discount = .30
    if(qty>1): discount=0.5
    amt = price*qty
    finalAmt = amt*(1-discount)
    return(finalAmt);
    
get_finalAmt(1000,2)
get_finalAmt(1000,1)
get_finalAmt(1000,3)


# case - 2 - write python code to find HRA amt to be paid
#based on below condition
# Salary_range     HRA_per
# 0-10000           30%
# 10000-30000       25%
# 30000-above       22%

x=int(input("enter x "))
if (x>=0 and x<=10000):
    print(x-(x*0.30))
elif(x>=10000 and x<=30000):
    print(x-(x*0.25))
elif(x>=30000):
    print(x-(x*0.22))
else:
    print("enter correct number")
        

#while = is used to execute python statements while given
# condition is true
# execute fpr true conditiin and stop for false condition
        
# =============================================================================
# while(condition):
#     python statements
# else:
#     python statements
# =============================================================================

time = 10
while(time<12):
    print("good morning")
    time=time+1
else:
    print("good afternoon")


# find number of days required to accumulate 5000/- if 
# i am saving 55/- per day
    
total=0;day=0
while (total<=5000):
    total+=55
    day+=1
print("Number of days is " +str(day))

# case 3 - find number of months need to get 500000/- if 
# i deposite 1000/- per month in bank every month. bank  roi is 7%.
# interest compounded monthly.

total=0;month=0
while (total<=500000):
    total+=1000
    total+=total*7/100
    month+=1
print("Number of month is " +str(month))






# if i am depositing my money in bank, and bank gives 8% interest per year.
# find how many year it will take to get 500000
# if i am depositing 20000/- per year.


total=0;year=0
while (total<=500000):
    total+=20000
    total+=total*8/100
    year+=1
print("Number of years is " +str(year))
    
# by function method

def req_years(peryear,reqamt,roi):
    year=0;amount=0
    while(amount<=reqamt):
        amount+=peryear
        amount+=amount*roi/100
        year+=1
    return(year);
        
req_years(20000,500000,8)
req_years(20000,600000,8.5)

# A person want to loose weight, currently he is 110kg
# he want to be 70kg, if he loose 3 kg in 11 days,
# then how many weeks it will take to ger desired weight.


curr_weight=110;days=0
while(curr_weight>=70):
        curr_weight-=3
        days+=11
print("number of days " + str(days))
weeks=day/7
print("number of weeks " + str(weeks)) 


def req_weeks(current_wt,loose_wt_perday,indays,req_wt):
    day=0
    while(current_wt>=req_wt):
        current_wt-=loose_wt_perday
        day+=indays
    weeks=day/7
    return weeks

req_weeks(110,3,11,70)


# =============================================================================
# for loop-- is used to execute set of instructiobs for each item in collection suntex:
#     for item in colllection:
#         python statements
# 
# =============================================================================

for i in [10,20,30]:
    print(i)

# write python code to increment all values in list by 10
# create list as follows[1,11,21,31,41]
empty_list2=[]   
new_list=[1,11,21,31,41]
for i in new_list:
    print(i+10)
    empty_list2.append(i)
print(empty_list2)



# =============================================================================
# create a function to find yearly balance if i am depositing 1000/-
# per month
# for 5 years in bank and bank is giving 4% interest per annum:
#     assime interest is compoundded monthly
# =============================================================================


def yearly_balance(permonth,year,roi):
    iteration=year*12
    amt=0
    for  i in range(1,iteration+1):
        amt+=permonth
        amt+=amt*roi/(12*100)
    return amt

yearly_balance(1000,5,4)


def yearly_deposite(monthly,year,roi):
    amt=0
    peryearamt=[]
    for y in range(1,year+1):
        for m in range(1,13):
            amt=amt+monthly
            amt=amt+amt*float(roi)/1200
        peryearamt.append(round(amt))
    return(peryearamt);
    
    
print(yearly_deposite(1000,5,4))













