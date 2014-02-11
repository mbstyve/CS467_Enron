__author__ = 'Michael'

import string
from collections import Counter
from operator import itemgetter

def word_frequency(body):
    out = body.translate(string.maketrans("", ""), string.punctuation)  ##gets rid of extraneous punctuation
    body_split = out.split()  ##splits up the paragraph by each individual word
    c=Counter(x.strip() for x in body_split)  #counter for each word
    for y in c.most_common():  ##sorts it by most common
        print y


def dateParser(JSONobject):
    indexOf200 = JSONobject['headers']['Date'].index('200')
    onlyDate = JSONobject['headers']['Date'][:indexOf200+4]
    return onlyDate

