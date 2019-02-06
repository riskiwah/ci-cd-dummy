from flask import Flask
app = Flask(__name__)

@app.route("/cicd")
def hello():
    return "Hello world jenki-kastem"

if __name__ == "__main__":
    app.run(host='0.0.0.0')