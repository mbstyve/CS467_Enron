__author__ = 'Michael'

import json

def dumpJSON(date, dataJSON):
    email = getEmail(dataJSON)
    dump={'total':{'scrimmage':2, 'other_test':3}, email:{'scrimmage':2, 'other_test':3}}
    test=json.dumps(dump)
    with open('JSON dump/Tue, 14 Nov 2000.txt', 'w') as outfile:
        json.dump(dump, outfile)

def getEmail(dataJSON):
    return dataJSON['headers']['From']

#dumpJSON('','')