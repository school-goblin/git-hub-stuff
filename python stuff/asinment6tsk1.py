import random 
import math
import time

num = 1
total = 0
fluky = 0

for loopnum in range(1,10001):
    total = 0
    if fluky == 7:
        break
    for i in range(1, loopnum):
        if loopnum % i == 0:
            random.seed(i)
            rannum1 = random.randint(1,loopnum)
            total += rannum1
    
    if total == loopnum:
        print(loopnum)
        fluky += 1

    
