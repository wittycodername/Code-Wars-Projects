# 6 kyu Delete occurrences of an element if it occurs more than n times

def delete_nth(order,max_e):

    a = []

    n = len(order)


    for i in range (0,n):
      
      b = a
      p = order[i]
      a.append(p)
      z = a.count(p)
      if z > max_e:
        del a[-1]

    return(a)