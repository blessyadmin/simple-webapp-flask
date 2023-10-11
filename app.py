import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'
    color = "red"
@app.route("/")
def main():
print(color)
return render_template('hello.html', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
