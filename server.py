from flask import Flask, render_template, jsonify, request
# import Transformation
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)