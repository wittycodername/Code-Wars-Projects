
# 5 kyu What's a Perfect Power anyway?

import math

def isPP(n):
    #your code here

    for i in range(2, n ):
        if n % i == 0:
               for k in range(2,8):
                  if i**k == n:
                     return([i,k])
                  
