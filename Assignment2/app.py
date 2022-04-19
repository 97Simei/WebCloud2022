from contextlib import nullcontext
from email import header
from http.client import FORBIDDEN
import re
from functools import wraps
from types import MethodType
from wsgiref.util import request_uri
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request, get_jwt
from flask import Flask, render_template, request, redirect, jsonify, make_response, url_for, redirect
from hashids import Hashids

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "LisimeiAssignmet2"
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
            if user['sub'] in USERPWD.keys():
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Not Registered!"), 403
        return decorator

    return wrapper


@app.route('/<string:hashid>/', methods=('GET', 'POST', 'DELETE', 'PUT'))
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
            return hashid,200
    if request.method == 'GET':
        if hashid in URLS.keys():
            return redirect(URLS[hashid], 301)
        else:
            print("no hashid:"+hashid)
            return render_template('404.html'), 404


@app.route('/', methods=('GET', 'POST', 'DELETE'))
@login_required()
def modifyShortUrl():
    current_user_id = get_jwt_identity()
    user = USERPWD[current_user_id]
    print("User:"+user)
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

def home():
    return render_template('home.html')

# login url
@app.route('/users/login', methods=('GET', 'POST'))
def login():
    global access_token
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['psw']
        if uname in USERPWD.keys() and USERPWD[uname] == pwd:
            access_token = create_access_token(identity=uname)
            return jsonify(({"token": access_token})), 200
        else:
            return make_response(jsonify({"msg": "FORBIDDEN"}), 403)
    return render_template('login.html')


@ app.route('/users', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['psw']
        pwdc = request.form['pswc']
        if pwdc == pwd and uname not in USERPWD.keys():
            USERPWD[uname] = pwd
        return redirect(url_for('login'))
    return render_template('register.html')
