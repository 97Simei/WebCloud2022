from contextlib import nullcontext
from email import header
from http.client import FORBIDDEN
import re
from functools import wraps
from types import MethodType
from wsgiref.util import request_uri
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request, get_jwt
from flask import Flask, render_template, request, redirect, jsonify, make_response, url_for, redirect, session
from hashids import Hashids
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.secret_key = "27eduCBA09"
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["JWT_SECRET_KEY"] = "LisimeiAssignmet2"
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# CORS(app)
jwt = JWTManager(app)

hashids = Hashids()
URLS = {}
USERPWD = {}
USERJWT = {}

access_token = ''
id = 0


def get_key(val):
    for key, value in URLS.items():
        if val == value:
            return key
    return "key doesn't exist"


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


def login_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = get_jwt()
            if user['sub']:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Not Registered!"), 403
        return decorator

    return wrapper


@app.route('/<string:hashid>', methods=('GET', 'POST', 'DELETE', 'PUT'))
@cross_origin()
@login_required()
def handleId(hashid):
    if request.method == 'DELETE':
        if hashid in URLS.keys():
            del URLS[hashid]
            return URLS, 200
        else:
            return render_template('404.html'), 404
    if request.method == 'PUT':
        url = request.headers['url']
        if isValidURL(url) == False:
            shorturl = ''
            return "error", 400
        if hashid not in URLS.keys():
            return render_template('404.html'), 404
        else:
            if url in URLS.values():
                key = get_key(url)
                del URLS[key]
            URLS[hashid] = url
            shorturl = request.host_url + hashid
            print("New shortURL:"+shorturl)
            return jsonify({'url': URLS[hashid]}), 200
    if request.method == 'GET':
        print(hashid)
        if hashid in URLS.keys():
            print(URLS[hashid])
            return URLS[hashid]
        else:
            print("no hashid:"+hashid)
            return render_template('404.html'), 404


@app.route('/', methods=('GET', 'POST', 'DELETE'))
@cross_origin()
@login_required()
def modifyShortUrl():
    current_user_id = get_jwt_identity()
    print("User:" + current_user_id)
    global URL, URLS, shorturl
    if request.method == 'GET':
        return jsonify(URLS), 200
    if request.method == 'POST':
        global id
        url = request.form['url']
        if isValidURL(url) == False:
            shorturl = ''
            return "error", 400
        else:
            id = id+1
            hashid = hashids.encode(id)
            if url in URLS.values():
                key = get_key(url)
                del URLS[key]
            URLS[hashid] = url
            shorturl = request.host_url + hashid
            return hashid, 201
    if request.method == 'DELETE':
        URLS = {}
        id = 0
        return render_template('404.html'), 404

