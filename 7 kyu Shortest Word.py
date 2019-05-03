# 7 kyu Shortest Word

def find_short(s):
    x = s.split()
    y = [0]*len(x)
    z = len(x)
    for i in range(0,z):
        y[i] = len(x[i])

    y.sort()
    l = y[0]
    
    # your code here
    return l # l: shortest word length