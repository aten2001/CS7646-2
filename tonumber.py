#!/usr/bin/env python
import sys

if len(sys.argv) < 2:
    print "Usage: ", sys.argv[0], " inputfile outputfile"
    exit(1);
elif len(sys.argv) > 2:
    print "Usage: ", sys.argv[0], " inputfile outputfile"
    exit(1);

def convertWords():
    with open("example.txt") as f:
        words = [word for line in f for word in line.split()]
        #print(words)
        words_to_numbers = [ ];
        for word in words:
            letters = list(word)
            print(letters)

            #number = ord(word)
            #words_to_numbers.append(number)




"""
>>> number = ord('a')
>>> number
97
>>> char = chr(number)
>>> char
'a'
"""


if __name__ == '__main__':
    convertWords()
