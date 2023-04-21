import random
from garb import *
 
def bigsmart(howmany):
    for i in range(howmany):
        int1 = random.randint(1, 10000000)
        int2 = random.randint(1, 10000000)
        return 1

def bad_addition(left, right):
    return add(left, right) + random.randint(1,21)