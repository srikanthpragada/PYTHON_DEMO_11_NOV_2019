import os
import sys

if len(sys.argv) > 1:
    start = sys.argv[1]
else:
    start = input("Enter start directory :")
    # start = r"e:\classroom\python\nov11"

for (dir, dirs, files) in os.walk(start):
    for f in files:
        if f.endswith(".py"):
            print(dir + "\\" + f)
