from contextlib import nullcontext
from email import header
import re
from functools import wraps
from types import MethodType
from wsgiref.util import request_uri
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from flask import Flask, render_template, request, redirect, jsonify, make_response, url_for, redirect,session
app = Flask(__name__)
CORS(app, supports_credentials=True)
cors = CORS(app, resources={r"/*": {"origins":'*'}})
app.config["JWT_SECRET_KEY"] = "LisimeiAssignmet2"
app.secret_key = "27eduCBA09"
jwt = JWTManager(app)

USERPWD = {}

access_token = ''

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