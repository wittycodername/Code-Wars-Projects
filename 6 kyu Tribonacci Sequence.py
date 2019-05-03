# 6 kyu Tribonacci Sequence


def tribonacci(signature, n):
    if n==0:
      return []
    elif n==1:
       return [signature[0]]
    elif n==2:
       return [signature[0],signature[1]]
    elif n==3:
       return [signature[0],signature[1],signature[2]]
    else:
    
       a = signature[0]
       b = signature[1]
       c = signature[2]
       y= [a,b,c]
       l=len(y)
       while l<n:
           
           a, b, c = b, c, a+b+c
           y.append(c)
           l = l+1
       return y