
# 7 kyu List Filtering


def filter_list(l):
  'return a new list with the strings filtered out'
  n = len(l)
  x=[]
  for i in range (1,n+1):
      a = l[i-1]
      if type(a) == int:
        x.append(a)

  return x