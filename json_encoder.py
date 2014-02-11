__author__ = 'Michael'

import json

def dumpJSON(date, dataJSON):
    dump={'total':{'scrimmage':2, 'other_test':3}}
    test=json.dumps(dump)
    print test
    print dump['total']['scrimmage']
    with open('JSON dump/Tue, 14 Nov 2000.txt', 'w') as outfile:
        json.dump(dump, outfile)

dumpJSON('','')