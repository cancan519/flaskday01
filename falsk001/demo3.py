# coding=utf-8
from flask import Flask, session
from setting import Config
# 拓展包，作用式指定session的信息存放的位置，对session信息进行签名
#指定过期时间
# from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# Session(app)


@app.route('/setsession')
def set_session():
    session['name'] = 'python24'
    return 'set session success'

@app.route('/getsession')
def get_session():
    return session.get('name')

if __name__ == '__main__':
    app.run()