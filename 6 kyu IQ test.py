
# 6 kyu IQ Test

def iq_test(numbers):

  x = [int(s) for s in numbers.split(' ')]
  n = len(x)
  odd = []
  even = []
  a = 0
  b = 0
  for i in range (0,n):
      z = x[i]
      y = z%2
      if y ==0:
          even.append(z)
          a = i+1
      else:
        odd.append(z)
        b = i+1
  if len(odd)==1:
        return(b)
  else:
        return(a)