
# 6 kyu Vasya - Clerk

def tickets(people):

  n = len(people)
  x = 0
  y = 0
  a = 0

  if people[0] != 25:
    return("NO")

  for i in range (0,n):
    
    
    if people[i] == 25:
        x = x + 1
        a = a + 1

    elif people[i] == 50:
        if x == 0:
          return("NO")
        else: 
          x = x - 1
          y = y + 1
          a = a + 1
         

    elif people[i] == 100:
        if x == 0:
          return("NO")
        elif y >= 1:
          x = x - 1
          y = y - 1
          a = a + 1
        elif x >= 3:
          x = x - 3
        else:
          return("NO") 


  if a >= n-1:
    return("YES")