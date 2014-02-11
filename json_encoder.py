__author__ = 'Michael'

import json

dump={'total':{'scrimmage':2, 'other_test':3}}
test=json.dumps(dump)
print test
print dump['total']['scrimmage']