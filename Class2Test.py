
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

@app.route('/profile/<uid>')
def profile(uid):
    return "profile:" + uid

if __name__ == '__main__':
    app.run(debug=True)