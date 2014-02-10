__author__ = 'Michael'

import string
from collections import Counter
from operator import itemgetter

def word_frequency(body):
    out = body.translate(string.maketrans("", ""), string.punctuation)
    body_split = out.split()
    c=Counter(x.strip() for x in body_split)
    #for word in body_split:
        # do something useful with word
        #print word
        #d[word]
    #sorted(c.items())
    print c #
    for y in c.most_common():  ##sorts it by most common
        print y
