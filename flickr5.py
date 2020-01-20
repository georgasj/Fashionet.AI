# First, you should install flickrapi
# pip install flickrapi

import flickrapi
import urllib
import urllib.request
from PIL import Image
import time
import sqlite3

conn = sqlite3.connect('fashionist.db')
cur = conn.cursor()

# Flickr api access key
flickr=flickrapi.FlickrAPI('insert userkeys here', 'insert userkeys here', cache=True)

keyword = 'blouse'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=5,           # may be you can try different numbers..
                     sort='relevance')
#print(type(photos))
#<class 'generator'>
#print(photos)
#<generator object data_walker at 0x038A9150>

cur.execute('''
CREATE TABLE IF NOT EXISTS  (Class TEXT, Link TEXT)''')


urls = []
count = 0
for photo in photos:
    #print (i)

    url = photo.get('url_c')

    #(if we seen this before continue) we need to store in data base so we mine the results instead of starting again over and over!!

    if url != None:
        print(str(url))
        urllib.request.urlretrieve(url, str(count)+".jpg")
        image = Image.open(str(count)+".jpg")
        image = image.resize((256, 256), Image.ANTIALIAS)
        image.save(str(count)+".jpg")
        #urls.append(url)
        count = count + 1
        time.sleep(0.5)
        #print(urls)
    if count > 5:
        break
