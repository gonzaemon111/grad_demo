from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
import cv2
from datetime import datetime
from jinja2 import FileSystemLoader
import os, sys
import string
import random
import inspect
import base64
import numpy as np
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
@app.route('/image/transform', methods=['POST'])
def api_image():
    count = 0
    image = request.files['sample.jpg']
    stream = image.stream
    name = str(count) + '_' + image.name
    print(name)
    path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    print("------------1")
    img = cv2.imdecode(img_array, 1)
    cv2.imwrite(path, img)
    print("------------2")
    # print(url_for(url_path))
    return_name = Transformation.transform(name)
    # return redirect(url_for(uploaded_file(name)))
    count = count + 1
    # return send_from_directory('./resized', return_name)
    return send_from_directory('./resized', "hoge_resize.jpg")

@app.route("/upload", methods = ["POST"])
def upload():
    image = request.files['sample.jpg']
    stream = image.stream
    name = image.name
    print("------------1")
    print(name)
    print("------------2")
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    print("------------3")
    img = cv2.imdecode(img_array, 1)
    print("------------4")
    path = './tmp/' + name
    print("------------5")
    cv2.imwrite(path, img)
    print("------------6")
    # return send_from_directory('./transformed', name)
    return jsonify({ 'data': name })

@app.route("/demo", methods=["POST"])
def demo():
    image = request.files['sample.jpg']
    stream = image.stream
    name = image.name
    print(name)
    img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)
    path = './tmp/' + name
    cv2.imwrite(path, img)
    print("demo------------6")
    return_name = Transformation.transform(name)
    # return send_from_directory('./transformed', name)
    return jsonify({ 'data': return_name })

@app.route('/upload/<filename>')
def get_image(filename):
    print(filename)
    # return send_from_directory('./transformed', "2_perfect.jpg")
    return send_from_directory('./transformed', "7_perfect.jpg")


# return send_from_directory('./transformed', "hoge_resize.jpg")
# return send_from_directory('./transformed', "2_perfect.jpg")
# return send_from_directory('./transformed', "3_perfect.jpg")
# return send_from_directory('./transformed', "7_perfect.jpg")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)