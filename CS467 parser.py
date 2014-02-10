__author__ = 'Michael'

from pymongo import MongoClient
from word_frequency import word_frequency
import unicodedata

client = MongoClient('ec2-54-84-86-116.compute-1.amazonaws.com', 27017)
db = client['enron']
collections=db.messages  #accesses the enron "messages"
posts = collections.find_one()  #finds the first message
print posts
#print posts['body']
normalized_body=unicodedata.normalize('NFKD', posts['body']).encode('ascii','ignore')
word_frequency(normalized_body) ## #