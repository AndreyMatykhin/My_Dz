import sys

with open('bakery.csv', 'a', encoding="utf-8") as f:
    f.write(sys.argv[1]+"\n")
