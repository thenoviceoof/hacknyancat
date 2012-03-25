#!/usr/bin/env python

"""
Python wrapper, tumblr, list photos on nyancatwashere tumblr.

API Documentation:
http://www.tumblr.com/docs/en/api/v2#posts
"""

from config import TUMBLR_API_KEY

API_KEY = TUMBLR_API_KEY


try:
    import json
except ImportError:  # pragma: no cover
    # For older versions of Python.
    import simplejson as json

try:
    from urllib import urlencode
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import urlencode

try:
    from urllib import quote
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.parse import quote

try:
    from urllib2 import urlopen
except ImportError:  # pragma: no cover
    # For Python 3.
    from urllib.request import urlopen

import requests


class Tumblr_API(object):
    """Hacked single-use wrapper for Tumblr API"""

    def __init__(self):
        """Base URLs should have no '/' at the end"""
        self.base_url = ''

    def call_api(self, directory):
        url_list = [self.base_url]
        url_list.append('/posts/photo?&api_key=%s' % API_KEY)
        url_list.append('&%s' % str(directory))
        url = ''.join(url_list)
        print url
        r = requests.get(url)
        j = json.loads(r.content)
        #proposals = j["proposals"]
        #results = [x["title"] for x in proposals]
        #return results


class Posts(Tumblr_API):

    def __init__(self):
        self.base_url = 'http://api.tumblr.com/v2/blog/'

    def PhotosFromUser(self, username):
        """
        http://api.tumblr.com/v2/blog/nyancatwashere.tumblr.com/posts/photo?&api_key=
        """
        url = '%s.tumblr.com' % (username)
        return self.call_api(url)

""" to use:
import tumblr_api
from tumblr_api import (Tumblr_API, Posts)
testAPI = tumblr_api.Posts()
testAPI.PhotosFromUser('nyancatwashere')
"""
