from flask import Flask, render_template, url_for, request, redirect, jsonify
app = Flask(__name__)

a = 5


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route('/getdata', methods=["POST", "GET"])
def getdata():
    return str(a)

@app.route('/change/<x>/', methods=["POST", "GET"])
def change(x):
    global a
    a = x
    return str(a)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5000)


