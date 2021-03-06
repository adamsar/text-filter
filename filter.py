#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ftfy
import sys

def massage(data):
    lines = data.split("\n")
    numberless = []
    #Remove numbers
    for line in lines:
        split = line.split("\t")
        no_numbers = " ".join(split[1:]).strip()
        numberless.append(no_numbers)

    #Remove bad characters
    lines = [
        re.sub('[^a-zA-Z| |\']', ' ',  ftfy.fix_text(l.decode('utf-8'))) for l in numberless
        ]

    #fold data into a sentence structure.
    good_data = []
    for l in lines:
        while '  ' in l:
            l = l.replace('  ', ' ')
        good_data.append(l)            
    
    return "\n".join(good_data)


if __name__ == "__main__":
    f = sys.argv[1]
    print massage(open(f, 'r').read())
