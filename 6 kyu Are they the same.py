
# 6 kyu Are they the "same"?

def comp(array1, array2):


  if array1==None or array2==None:
     return False
     
  array1.sort()
  array2.sort()

  x = len(array1)

  if array1==[] or array2==[]:
     return True

  for i in range (0,x):
    array1[i] = array1[i]**2
    
  for i in range (0,x):
    if array1[i] != array2[i]:
      return False
      break
  else:
      return True