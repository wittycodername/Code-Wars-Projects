

def find_uniq(arr):

    arr.sort()
    
    if arr[0] == arr[1]:
        n = arr[-1]
    else:
        n = arr[0]
    # your code here
    
    return n   # n: unique integer in the array