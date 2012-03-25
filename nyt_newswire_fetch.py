#!/usr/bin/python
################################################################################
# this fetches NYT newswire stuff every 20 minutes (duck under the
# 5000 daily rate limit

import requests
import json
import time
import re

from config import NYT_API_KEY, PARSELY_API_URL

API_KEY = NYT_API_KEY

# get 20 
# {version}/content/src/sect/hrs.format?api-key=#
"http://api.nytimes.com/svc/news/v3/content/all/all/24.json?api-key=####"
url = "http://api.nytimes.com/svc/news/v3/content/\
all/all/24.json?api-key={apikey}&offset={offset}".format(apikey=API_KEY,
                                                         offset=0)

r = requests.get(url)
j = json.loads(r.content)

results = j["results"]
titles = [res["title"] + ": " + res["abstract"] for res in results]
title_str = " | ".join(titles)

########################################
# join titles, push up to parse.ly

r = requests.post(PARSELY_API_URL+"parse", {"text": title_str})
status_url = json.loads(r.content)["url"][1:]

i = 1
r = requests.get(PARSELY_API_URL+status_url)
status = json.loads(r.content)
while status["status"] != "DONE":
    i *= 2
    time.sleep(i)
    # reget the parse
    r = requests.get(PARSELY_API_URL+status_url)
    status = json.loads(r.content)

data= re.sub("<TOPIC>.*?</TOPIC>",
             "<img src ='http://farm6.staticflickr.com/5149/buddyicons/1636317@N24.jpg?1303318659'></img>",
             status["data"]);
print data
