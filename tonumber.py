#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print "Usage: ", sys.argv[0], " inputfile outputfile"
    exit(1);
elif len(sys.argv) > 2:
    print "Usage: ", sys.argv[0], " inputfile outputfile"
    exit(1);

def openFile():
    with open("example.txt") as f:
        words = [word for line in f for word in line.split()]
        print(words)

print(words)

"""
>>> number = ord('a')
>>> number
97
>>> char = chr(number)
>>> char
'a'
"""


if __name__ == '__main__':
    openFile()
