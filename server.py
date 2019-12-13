from flask import Flask, render_template, jsonify, request
import cv2
from datetime import datetime
import os
import string
import random
# import Transformation
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
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
    print(request.files['file'].filename)
    new_user = {}
    for file in request.files:
        if file is None:
            break
        upload_file = request.files.get(file)
        upload_path = 'data/%s' % upload_file.filename
        upload_file.save(upload_path)
        new_user[file] = upload_file.filename
        return jsonify(new_user)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)