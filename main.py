from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'dev': 'python',
        'message': 'Hello World!'
    })

if __name__ == '__main__':
    app.run()