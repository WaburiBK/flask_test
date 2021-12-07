from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/Brian')
def Brian():
    return "hello Brian"

@app.route('/Projects')
def Projects():
    return "Here is a list of my projects!"


if __name__ == '__main__':
    app.run(debug=True)