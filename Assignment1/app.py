import copy
import json
import re
from flask import Flask, abort, render_template, request, url_for, flash, redirect
from hashids import Hashids

app = Flask(__name__)

hashids = Hashids()
URLS={}


id = 0

def isValidURL(str):
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False

#show all the URLs
@app.route('/URLList', methods=('GET','POST'))
def showUrls():
    if request.method == 'GET':
        return URLS
#shorten url to original url
@app.route('/<string:hashid>/',methods=('GET','POST'))
def redirectURl(hashid):
    myurl = request.host_url + hashid
    if hashid in URLS:
        return redirect(URLS[hashid])
    else:
        listurl = request.host_url+'URLList'
        return render_template('404.html', home_url=request.host_url ,list_url=listurl), 404
#delete url
@app.route('/delete/<string:hashid>',methods=['GET'])
def deleteURl(hashid):
    del URLS[hashid]
    return URLS

#delete all

@app.route('/delete/All',methods=['GET'])
def deleteAllURl():
    URLS={}
    id = 0
    return "<p>Database is empty.</p>"
#default
@app.route('/', methods=('GET', 'POST'))
def createShortUrl():
    global URL
    if request.method == 'POST':
        global id
        url= request.form['url']

        if isValidURL(url) == False:
            shorturl = ''
            return render_template('index.html', url_false = True)

        else:
            url_false = False
            id = id+1
            hashid = hashids.encode(id)
            URLS[hashid] = url
            shorturl = request.host_url + hashid
            return render_template('index.html', short_url=shorturl)
    return render_template('index.html')

