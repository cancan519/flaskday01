# coding=utf-8
from flask import Flask,session
from flask import request
from setting import Config
# 拓展包，作用式指定session的信息存放的位置，对session信息进行签名
#指定过期时间
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
Session(app)


@app.route('/setsession')
def set_session():
    session['name'] = 'python24'
    return 'set session success'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/projects/',methods=['GET','POST'])
def projects():
    if request.method == 'POST':
        return 'The project page'
    else:
        return 'a'



if __name__ == '__main__':
    app.run(debug=True)



