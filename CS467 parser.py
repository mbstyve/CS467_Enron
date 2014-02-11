__author__ = 'Michael'

from pymongo import MongoClient
from word_frequency import word_frequency
from collections import Counter
from word_frequency import dateParser
import json

import unicodedata
from json_encoder import dumpJSON

client = MongoClient('ec2-54-84-86-116.compute-1.amazonaws.com', 27017)
db = client['enron']
collections = db.messages  #accesses the enron "messages"
posts = collections.find_one()  #finds the first message
print posts

 #pass in string to word_frequency to count
posts2 = collections.find()  #should get ALL emails in the database

# c = word_frequency(posts2[0]['body'])
# for y in c.most_common():  ##sorts it by most common
#     print y
# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
# c2 = word_frequency(posts2[1]['body'])
# for y in c2.most_common():  ##sorts it by most common
#     print y
# c3=c+c2
# print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
# for y in c3.most_common():  ##sorts it by most common
#     print y

posts10=posts2
cFinal=Counter()
allDates = {}

for x in posts10:
    date = dateParser(x)
    if date is None:
        continue
    c = word_frequency(x['body'])
    if allDates.has_key(date):
        cDict=allDates.get(date)
        cDict = cDict+c
        allDates[date]=cDict
    else:
        allDates[date]=c

# for y in allDates:
#     print allDates[y]

with open('JSON dump/stuff.txt', 'w') as outfile:
        json.dump(allDates, outfile)

print len(allDates)
print 'done'
#print posts2.count()
# print posts2[0]['headers']['Date']
# date = dateParser(posts2[3])
# dumpJSON(date, posts2[0])