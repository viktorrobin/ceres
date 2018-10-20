#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# @app.route('/todo/api/v1.0/tasks', methods=['GET'])
@app.route('/api/<path_pic>', methods=['GET', 'POST'])
def get_tasks(path_pic):
    from catDetector import predict_proba_catInPic
    proba = predict_proba_catInPic(path_pic)
    dicOut = {
        'picture': path_pic,
        'probaCat': float(proba)
    }
    return jsonify(dicOut)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
