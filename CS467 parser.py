__author__ = 'Michael'

from pymongo import MongoClient
from word_frequency import word_frequency
from word_frequency import dateParser
import unicodedata
from json_encoder import dumpJSON

client = MongoClient('ec2-54-84-86-116.compute-1.amazonaws.com', 27017)
db = client['enron']
collections=db.messages  #accesses the enron "messages"
posts = collections.find_one()  #finds the first message
normalized_body=unicodedata.normalize('NFKD', posts['body']).encode('ascii','ignore')  #converts from unicode to string
word_frequency(normalized_body)  #pass in string to word_frequency to count
#posts2 = collections.find()  #should get ALL emails in the database
posts2=posts
#print posts2.count()
print posts2[0]['headers']['Date']
date = dateParser(posts2[0])
dumpJSON(date, posts2[0])