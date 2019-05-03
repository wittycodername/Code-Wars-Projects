
# 6 kyu Multiplication Tables

def multiplication_table(row,col):


    a = []
    b = []
    
    for j in range (1,row+1):
    
      for i in range (1,col+1):
        d = i*j
        a.append(d)
      b.append(a)
      a=[]
      
      
    return(b)