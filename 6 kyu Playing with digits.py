
# 6 kyu Playing with digits

def dig_pow(n, p):

  m = [int(d) for d in str(n)]
  j=0

  for i in range (0,len(m)):
    j = j + (m[i])**(p+i)
  print(j)

  k = j/n
  if k == int(k):
    return k
  else: 
    return -1