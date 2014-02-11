__author__ = 'Michael'

import string
from collections import Counter
from operator import itemgetter
import unicodedata

#given a body, counts the words and returns it as an array? (counter
def word_frequency(body):
    body=unicodedata.normalize('NFKD', body).encode('ascii','ignore')
    out = body.translate(string.maketrans("", ""), string.punctuation)  ##gets rid of extraneous punctuation
    body_split = out.lower().split()  ##splits up the paragraph by each individual word
    c=Counter(x.strip() for x in body_split)  #counter for each word
    #how to get it be descending order
    #for y in c.most_common():  ##sorts it by most common
    #    print y
    return c

#parses out the date given a JSON object from the database
def dateParser(JSONobject):
    indexOf200 = JSONobject['headers']['Date'].index('200')
    onlyDate = JSONobject['headers']['Date'][:indexOf200+4]
    return onlyDate

