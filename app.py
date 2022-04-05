import copy
import json
from flask import Flask, abort, render_template, request, url_for, flash, redirect
from hashids import Hashids
app = Flask(__name__)

hashids = Hashids()
URLS={}


id = 0
def abort_if_todo_doesnt_exist(hashid):
    if hashid not in URLS:
        abort(404, message="Shortened URL {} doesn't exist".format(hashid))

#show all the URLs
@app.route('/URLList', methods=('GET','POST'))
def showUrls():
    if request.method == 'GET':
        return URLS
#shorten url to original url
@app.route('/<string:hashid>/',methods=('GET','POST'))
def redirectURl(hashid):
    if request.method == "GET":
        abort_if_todo_doesnt_exist(hashid)
        return redirect(URLS[hashid])
#delete url
@app.route('/delete/<string:hashid>',methods=['GET'])
def deleteURl(hashid):
    del URLS[hashid]
    return URLS

#delete all

@app.route('/deleteAll',methods=['GET'])
def deleteAllURl():
    URLS={}
    return URLS
#default
@app.route('/', methods=('GET', 'POST'))
def createShortUrl():
    global URL
    if request.method == 'POST':
        global id
        url= request.form['url']
        if not url:
            flash('Url is Empty!')
        else:
            id = id+1
            hashid = hashids.encode(id)
            URLS["shorten"+hashid] = url
    return render_template('index.html')

