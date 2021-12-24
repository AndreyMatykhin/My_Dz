import sys
from itertools import islice

with open('bakery.csv', 'r', encoding="utf-8") as f:
    if len(sys.argv[1:]) == 1:
        print(''.join(islice(f, int(sys.argv[1]) - 1, None)))
    elif len(sys.argv[1:]) == 2:
        print(''.join(islice(f, int(sys.argv[1]) - 1, int(sys.argv[2]))))
    else:
        line = f.readline().strip()
        while line:
            print(line)
            line = f.readline().strip()
