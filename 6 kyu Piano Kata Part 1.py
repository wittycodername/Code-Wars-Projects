
# 6 kyu Piano Kata, Part 1

def black_or_white_key(key_press_count):

    x = key_press_count
    
    y = x % 88
    z = y % 12
    
    if y == 0:
       return ("white")
    elif z in [0, 2, 5, 7, 10]:
       return ("black")
    else:
       return ("white")
    
    # your code here