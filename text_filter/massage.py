#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import ftfy

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
    
    with_numbers = ["\t".join([str(i), l]) for i, l in enumerate(good_data)]
    return "\n".join(with_numbers)
