
# 6 kyu Tortoise racing

def race(v1, v2, g):

    if v1 >= v2:
        return None
    
    relvel = v2 - v1
    
    time = [None]*3
    timeinsecs = 3600*g/(relvel)
    

    h = int(timeinsecs/3600)
    m = int(60*(timeinsecs/3600-h))
    s = int(timeinsecs - 3600*h - 60*m)
    if s == 60:
        m = m+1
        s = 0
          
        if m == 60: 
             h = h+1
             m = 0
    
    

    time[0] = h
    time[1] = m
    time[2] = s

    return time 
    