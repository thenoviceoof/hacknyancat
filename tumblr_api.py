#!/usr/bin/python
import tumblpy as Tumblpy

from config import TUMBLR_API_KEY, TUMBLR_API_SECRET

API_KEY = TUMBLR_API_KEY
API_SECRET = TUMBLR_API_SECRET

t = Tumblpy(app_key = API_KEY,
            app_secret = API_SECRET,
            callback_url = 'http://example.com/callback/')

auth_props = t.get_authentication_tokens()
auth_url = auth_props['auth_url']

oauth_token = auth_props['oauth_token']
oauth_token_secret = auth_props['oauth_token_secret']

t = Tumblpy(app_key = API_KEY,
            app_secret = API_SECRET,
            oauth_token=session['tumblr_session_keys']['oauth_token'],
            oauth_token_secret=session['tumblr_session_keys']['oauth_token_secret'])
