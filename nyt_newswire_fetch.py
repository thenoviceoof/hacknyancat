#!/usr/bin/python
################################################################################
# this fetches NYT newswire stuff every 20 minutes (duck under the
# 5000 daily rate limit

import requests
import json

from config import NYT_API_KEY

API_KEY = NYT_API_KEY

# {version}/content/src/sect/hrs.format?api-key=#
"http://api.nytimes.com/svc/news/v3/content/all/all/24.json?api-key=####"
url = "http://api.nytimes.com/svc/news/v3/content/\
all/all/24.json?api-key={apikey}".format(apikey=API_KEY)

r = requests.get(url)
print(r.content)
j = json.loads(r.content)
