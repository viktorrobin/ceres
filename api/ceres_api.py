#!flask/bin/python
from flask import Flask, jsonify, request
from catDetector import predict_proba_catInPic
from PIL import Image

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test_api():
    return 'Success!'

@app.route('/api', methods=['GET', 'POST'])
def get_tasks():
    print(request)
    img = Image.open(request.files['image'])

    path_pic = '/tmp/testImageAPI.png'
    img.save(path_pic)
    proba = predict_proba_catInPic(path_pic)

    dicOut = {
        'picture': path_pic,
        'probaCat': float(proba)
    }
    return jsonify(dicOut)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
