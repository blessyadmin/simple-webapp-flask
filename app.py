import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

    @app.route("/who are you")
def main():
    return "iam ARUNA!"

    @app.route('/where r u from')
def hello():
    return 'IAM FROM VIZAG'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
