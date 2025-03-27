from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({
        'status': 'success',
        'message': 'API is running'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
