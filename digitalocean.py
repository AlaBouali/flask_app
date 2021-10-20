from flask import Flask, render_template, request,send_file,Response,url_for,redirect,session
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


flask_host='localhost'
flask_port=5000 



@app.route('/', methods = ['GET', 'POST'])
def hello():
 return "hello"


if __name__ == '__main__':
   app.run(host=flask_host,port=flask_port,debug = True)
