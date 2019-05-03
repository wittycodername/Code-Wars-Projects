
# 7 kyu Find the stray number

def stray(arr):
   x = max(arr, key = arr.count)
   a=len(arr)
   for i in range (0, a):
       b = arr[i]   
       if b != x:
           return b