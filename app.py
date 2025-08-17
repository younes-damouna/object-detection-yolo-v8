from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World h!</p>"

if __name__ in "__main__":
    app.run(debug=True)