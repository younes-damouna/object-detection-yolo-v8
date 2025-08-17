from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World h!</p>"

if __name__ in "__main__":
    app.run(debug=True)