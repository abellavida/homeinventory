import pprint
from googleapiclient.discovery import build
from datetime import datetime
from bson.json_util import loads
import json
from config import db, dbtemp, dbhInv
from models import RecipeSearch
from mongoengine import *



##client = MongoClient()
##db = client.homeinventory


my_api_key = "AIzaSyDsENtJ8XseGsUt9Mmnwm-HttztdLH3xBU"
my_cse_id = "010477098343863254254:q2cas3oqpqc"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
##    return res

##def keyCleaner(d):
##    if type(d) is dict:
##        for key, value in d.items():
##            d[key] = keyCleaner(value)
##            if '.' in key:
##                d[key.replace('.', '\u002E')] = value
##                del(d[key])
##        return d
##    if type(d) is list:
##        return map(keyCleaner, d)
##    if type(d) is tuple:
##        return tuple(keyCleaner, d)
##    return d


def recipe_search(username, terms):
##    search_terms = ('recipe %s' %terms)
    
    results = google_search(terms, my_api_key, my_cse_id, num=10)
    timestamp = datetime.utcnow()#.strftime("%Y-%d-%d %H:%M:%S")
   
   
    for result in results:
        r = RecipeSearch()
        r.username = username
        r.timestamp = timestamp
        r.displayLink = result['displayLink']
        r.link = result['link']
        r.htmlTitle = result['htmlTitle']
        r.title  = result['title']

        r.save()

        
##           data = {}
##           data['username'] = username
##           data['timestamp'] = timestamp
##           data['displayLink'] = result['displayLink']
##           data['link'] = result['link']
##           data['htmlTitle'] = result['htmlTitle']
####           data['pagemap']= result['pagemap']
##           data['title']= result['title']
##           pprint.pprint(data)
##           db.recipesearch.insert_one(data)


def main():
    username = input('Username ')
    terms = input('What ingredients do you have? ')
    recipe_search(username, terms)

if __name__ == '__main__':
    main()


