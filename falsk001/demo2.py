#coding=utf-8
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def demo1():
    return 'manager变态返回'


if __name__ == '__main__':
    manager.run()