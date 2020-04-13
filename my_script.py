from flask import Flask, jsonify
app = Flask(__name__)


apps = [
    results:{
        'name':'test',
        'gitUrl':'https://github.com/kkech/testRepoDeploy.git',
        'version':'1.0'
    },
    {
      'name':'test',
      'gitUrl':'https://github.com/kkech/testRepoDeploy.git',
      'version':'1.0'
    }
]

@app.route('/getVersion')
def hello_world():
    return jsonify({"apps": apps})
