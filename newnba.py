import config
import sys
import time
import praw
import datetime
import json

file_count = 0

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "lavar balls big game")
    return r

def freshest_news_nba(r):
    results = r.subreddit('nba').new(limit = 12)
    return results

def read_fresh(results):
    i = 1
    ignore = 0
    print(str(datetime.datetime.now()))
    title_arr = []
    for thread in results:
        if ignore == 0 or ignore == 1:
            ignore = ignore + 1
        else:
            print(str(i) +'.(' + thread.subreddit.display_name + '-'+ str(thread.ups) + ') '  + thread.title + '\n')
            title_arr.append(thread.title)
            i = i + 1
    data = {}
    data['headlines'] = title_arr
    data['last_hash_key'] = None
    json_data = json.dumps(data)
    print("____________________________________________________" + str(datetime.datetime.now()))
    return(json_data)

def save_to_json1(json_data1):
    file_object = open("title_obj1.json","w")
    file_object.write(json_data1)
    file_object.close

def save_to_json2(json_data2):
    file_object = open("title_obj2.json","w")
    file_object.write(json_data2)
    file_object.close

r = bot_login()

while True:
    save_to_json1(read_fresh(freshest_news_nba(r)))
    time.sleep(60)
    save_to_json2(read_fresh(freshest_news_nba(r)))
    time.sleep(60)

