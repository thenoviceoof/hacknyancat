#!/usr/bin/python
################################################################################
# this fetches NYT newswire stuff every 20 minutes (duck under the
# 5000 daily rate limit

from config import NYT_API_KEY

API_KEY = NYT_API_KEY

# {version}/content/src/sect/hrs.format?api-key=#
url = "http://api.nytimes.com/svc/news/{version}/content/\
all/all/10.json?api-key={api-key}"

