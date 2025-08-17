from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
model = YOLO("models/best.pt")

@app.route("/", methods=["GET", "POST"])
def index():
   
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)