# -*- coding:utf-8 -*-
import json

from flask import Flask,redirect,abort,render_template,session,url_for,request
app = Flask(__name__)


@app.route('/hello')
def do_hello():
    users = [{"username":"users1","url":"/users/user1"},
             {"username":"users2","url":"/users/user2"},
             {"username":"users3","url":"/users/user3"},
             {"username":"users4","url":"/users/user4"}
             ]
    return render_template("base.html",title="User list",users=users)

@app.route('/json')
def do_json():
    hello = {"name":"stranger" , "say" : "hello"}
    return json.dumps(hello)

@app.route('/gobaidu')
def do_baidu():
    return redirect('http://www.baidu.com')

@app.route('/login')
def do_log():
    login = '<h1>Username : <h1>'
    login = login + '<h1>Password : <h1>'
    return login

@app.route('/user/<username>')
def do_user(username):
    if username == 'felix':
        abort(404)
    return('User %s\' page ' % username)

@app.route('/child1')
def do_child():
    return render_template("child.html")

@app.route('/string')
def do_string():
    return render_template("string.html",user = "felix zeng")


@app.route('/numerics')
def numerics():
    return render_template("numerics.html",n1=3.14159,n2=29838721)

@app.route('/userdefined')
def userdefined():
    return render_template("userdefined.html",s="akcdefg")




@app.route("/")
def index():
    if session.get('username')=='shiyanlou' and session.get('password')=='shiyanlou':
        return "hello shiyanlou"
    return "you are not logged in"

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=='POST':
        session['username']=request.form['username']
        session['password']=request.form['password']
        return redirect(url_for('index'))
    return """
    <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=text name=password>
        <p><input type=submit value=Login>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect(url_for('index'))
