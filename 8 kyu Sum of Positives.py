
# 8 kyu Sum of positive

def positive_sum(arr):
# Your code here
    x = 0 
    for i in arr:
        if i > 0:
            x += i
    return x
    