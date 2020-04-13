
from flask import Flask, jsonify
app = Flask(__name__)

apps = [
    {
        'name':'test',
        'gitUrl':'https://github.com/kkech/testRepoDeploy.git',
        'version':'1.0'
    },
    {
      'name':'test1',
      'gitUrl':'https://github.com/kkech/testRepoDeploy.git',
      'version':'1.1'
    }
]

@app.route('/getVersion')
def hello_world():
    return jsonify({"apps": apps})

if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0')
