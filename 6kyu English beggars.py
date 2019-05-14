# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:21:47 2019

@author: mynam
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:21:07 2019

@author: mynam
"""

def beggars(values, n):


    if n == 0:
        ans = []

    else:
        ans = [0] * n
        y = len(values)
        z = int(y/n)
        t = y%n
    
        for i in range(0,n):
            for j in range(0,z):
                ans[i] += values[i+j*n]
        
        for i in range(0,t):
            ans[i] += values[z*n+i]
    return ans
    #your code here


