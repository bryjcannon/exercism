# -*- coding: utf-8 -*-
import re

def word_count(passage):
    passage = re.sub('[^a-zA-Z0-9\n\t ]', ' ', passage)
    words = [word.lower() for word in passage.split()]
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        elif word not in counts:
            counts[word] = 1
        else:
            print "Issue with word {}".format(word)
    return counts
