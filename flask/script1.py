from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    return "hello"

@app.route('/describe')
def describe():
    return 'description page here'

@app.route('/home/<name>')
def homePage(name):
    return f"Hello there, {name}"

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

@app.route('/home/<float:num>')
def floatDisplay(num):
    return jsonify({'data': num})

if __name__ == '__main__':
    app.run(debug= True)