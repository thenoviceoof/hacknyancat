#!/usr/bin/env python

"""
Python wrapper, donorschoose, find project listings by geo latlong.

API Documentation:
http://developer.donorschoose.org/documentation/project-listing/json-feeds/json-requests
"""

from config import DOCO_API_KEY

API_KEY = DOCO_API_KEY


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


class Doco_API(object):
    """Hacked single-use wrapper for Doco API"""

    def __init__(self):
        """Base URLs should have no '/' at the end"""
        self.base_url = ''

    def call_api(self, directory):
        url_list = [self.base_url]
        url_list.append('&APIKey=' + API_KEY)
        url = ''.join(url_list)
        data = urlopen(url).read()
        return json.loads(data)


class Geo(Doco_API):

    def __init__(self):
        self.base_url = 'http://api.donorschoose.org/common/json_feed.html?'

    def ProjectsNearLatLong(self, latitude, longitude):
        """
        >>> doco_api.geo().ProjectsNearLatLong(40.776104,-73.920822)
        http://api.donorschoose.org/common/json_feed.html?APIKey=DONORSCHOOSE&centerLat=40.776104&centerLng=-73.920822
        """
        url = 'centerLat=%s&centerLng=%s' % (latitude, longitude)
        return self.call_api(url)

# http://api.donorschoose.org/common/json_feed.html?APIKey=DONORSCHOOSE&centerLat=40.776104&centerLng=-73.920822
""" to use:
import doco_api
from doco_api import (Doco_API, Geo)
doco_api.Geo().ProjectsNearLatLong(40.776104,-73.920822)
"""