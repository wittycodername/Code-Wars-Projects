# 7 kyu Sum of odd numbers

def row_sum_odd_numbers(n):
    y=(n*n)-n+1
    x = y

    for i in range (1,n):
        y = y+ 2
        x = x + y
    return x