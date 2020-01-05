from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
import cv2
from datetime import datetime
from jinja2 import FileSystemLoader
import os, sys
import string
import random
import inspect
import base64
from transformation import Transformation
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = './tmp'
app.debug = True


@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/hello')
def hello_world():
    return jsonify({'message': 'Hello, world'})

@app.route('/', methods=['POST'])
def post_json():
    json = request.get_json()  # POSTされたJSONを取得
    print(json)
    return jsonify(json)  # JSONをレスポンス

@app.route('/images', methods=['POST'])
def post_image():
    print("root--------------")
    print(request.files['file'])
    new_user = {}
    print(inspect.getmembers(request.files))
    print("--------------")
    for file in request.files:
        if file is None:
            break
        upload_file = request.files.get(file)
        upload_path = 'data/%s' % upload_file.filename
        upload_file.save(upload_path)
        new_user["name"] = upload_file.filename
    return jsonify(new_user)

'''
imageのダウンロード
curl -X GET -o sample.jpg http://127.0.0.1:8080/image/transorm
↓ 本番
'''
@app.route('/image/transorm', methods=['POST'])
def api_image():
    img = request.files['image']
    name = img.filename
    path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    img.save(path)
    # print(url_for(url_path))
    print("------------1")
    return_name = Transformation.transform(name)
    # return redirect(url_for(uploaded_file(name)))
    return send_from_directory('./transformed', return_name)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)