#!/usr/bin/env python
import sys, string
"""
tonumber.py < file.txt > file.number
"""

def convertStringToAsciiCharacters(sentence):
    ascii_rep=[]
    for word in sentence:
        for char in word:
            ascii_rep.append(ord(char))
    return ascii_rep

if len(sys.argv) < 2:
    sys.stderr.write('Usage: sys.argv[0] \n')
    sys.exit(1)



f = open(sys.argv[1])
for word in f.read().split():
    lower = word.lower()
    for c in string.punctuation:
        lower=lower.replace(c,"")
    myword = convertStringToAsciiCharacters(lower)
    print ''.join(str(x) for x in myword)
