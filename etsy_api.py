#!/usr/bin/env python

"""
Python wrapper, etsy, find nyancat listings.

API Documentation:
http://www.etsy.com/developers/documentation/reference/listing
"""

from config import ETSY_API_KEY

API_KEY = ETSY_API_KEY

# http://openapi.etsy.com/v2/private/listings/active?keywords={keyword}&api_key=

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


class Etsy_API(object):
    """Hacked single-use Wrapper for Etsy API"""

    def __init__(self):
        """Base URLs should have no '/' at the end"""
        self.base_url = 'http://openapi.etsy.com/v2/private/'

    def call_api(self, directory):
        url_list = [self.base_url]
        url_list.append('&api_key=' + API_KEY)
        url = ''.join(url_list)
        data = urlopen(url).read()
        return json.loads(data)


class Listings(Etsy_API):

    def __init__(self):
        self.base_url = 'http://openapi.etsy.com/v2/private/listings/active?'

    def findAllListingActive(self, keywords):
        """
        >>> api.Licenses_And_Permits().by_category('doing business as')
        http://openapi.etsy.com/v2/private/listings/active?keywords=nyancat&api_key=
        """
        url = 'keywords=%s' % keywords
        return self.call_api(url)

""" to use:
import etsy_api
from etsy_api import (Etsy_API, Listings)
etsy_api.Listings().findAllListingActive('nyancat')
"""
