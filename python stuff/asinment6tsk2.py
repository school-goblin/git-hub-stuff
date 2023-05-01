#gaming

import random
import math
gmaing = True

while gmaing: 
    zofin0 = 0
    zofin1 = 0
    zofin2 = 0
    for i in range(100000):
        ele1 = random.randint(1,6)
        ele2 = random.randint(1,6)
        zokeep = random.randint(1,6)
        if zokeep == ele1 and zokeep == ele2:
            zofin2 += 1
        elif zokeep == ele1 or zokeep == ele2:
            zofin1 += 1
        else:
            zofin0 += 1
        i += 1
    zopin0 = (zofin0 / 100000) * 100
    zopin1 = (zofin1 / 100000) * 100
    zopin2 = (zofin2 / 100000) * 100
    print("he found no elephant " + str(zofin0) + " times")
    print("he found one elephant " + str(zofin1) + " times")
    print("he found two elephant " + str(zofin2) + " times")
    print("he found no elephant " + str(round(zopin0, 2)) + " % of the time")
    print("he found one elephant " + str(round(zopin1, 2)) + " % of the time")
    print("he found two elephant " + str(round(zopin2, 2)) + " % of the time")
    again = input("hit it again?")
    if again == "yes":
        gmaing = True
    else: 
        gmaing = False

print("Andrew has a bald head get rotated idiot.")
