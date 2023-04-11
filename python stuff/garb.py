def countBack(beg, step = 2, end = 0):
    counter = beg
    while(counter > end):
        print(counter)
        counter -= step

def countToNum(beg, step = 1, end = 100):
    count = beg
    while(count <= end):
        print(count)
        count += step

def main():
    countBack(10)

main()

