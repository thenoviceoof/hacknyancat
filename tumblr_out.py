#!/usr/bin/env python

import tumblr_api
from tumblr_api import (Tumblr_API, Posts)
testAPI = tumblr_api.Posts()
links = testAPI.PhotosFromUser('nyancatwashere')
f = open('./tempout.html', 'w')
end = [] 
for link in links:
        #end.append("<a href = '%s'>%s</a><br / ><br / >" % (link, link))
        end.append("<a href='%s'><img src='%s'></img></a><br / ><br / >" % (link, link))
ends = ''.join(end)
f.write(ends)
