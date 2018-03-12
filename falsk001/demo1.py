# coding=utf-8

from  flask import Flask,jsonify,abort,redirect,url_for
from setting import Config

app = Flask(__name__)
app.config.from_object(Config)

import json

@app.route('/demo1')
def demo1():
    return 'demo1', 405

@app.route('/')
def demo2():
    abort(404)
    return 'demo2', 403

@app.errorhandler(404)
def demo3(e):
    return '页面找不到'


@app.route('/redirect')
def demo4():
    return redirect(url_for('demo'))


@app.route('/json')
def demo():
    my_dict = {"name":"DongGe","age":20}
    # return json.dumps(my_dict)
    return jsonify(my_dict)


if __name__ == '__main__':
    app.run()