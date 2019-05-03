# 7 kyu Power of Two

import math
def power_of_two(x):
    y = math.log(x, 2)
    z = math.floor(y)
    a = 2**z

    if a == x:
        return (True)
    else:
        return (False)