# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:09:18 2019

@author: Mohit
"""

# =============================================================================
# loop control statemnts
# break-will stop the loop
# continue- will stop current iteration and continue for next 
# pass - will pass execution to next statement, it will do nothing
# =============================================================================

for i in "python":
    print(i)
    
for i in "python":
        if (i=="t"):break
        print(i)
        
for i in "python":
    if (i=="t"):continue
    print(i)
    
for i in "python":
    if (i=="t"):pass
    print(i)