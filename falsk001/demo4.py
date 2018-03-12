#coding=utf-8

from flask import Flask,render_template
from setting import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def demo1():
    temp = {"user":"python24","age":18}
    list_info =[14,22,35]
    return render_template('index.html',temp=temp,list_info=list_info)

if __name__ == '__main__':
    app.run()