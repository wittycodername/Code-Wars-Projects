
# 7 kyu Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    sorted(numbers)
    numbers.sort()
    x = 0
    if numbers[0] > 0:
           x += numbers[0]
           if numbers[1] > 0:
             x += numbers[1]
    return x
    #your code here