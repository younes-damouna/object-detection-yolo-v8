from flask import Flask, render_template, request, redirect, url_for
from ultralytics import YOLO
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
model = YOLO("models/best.pt")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            filename = str(uuid.uuid4()) + ".jpg"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Run prediction
            results = model.predict(source=filepath, save=True, project="static/results", name="run", exist_ok=True)

            # Get result image path
            result_path = results[0].save_dir + "/" + os.path.basename(filepath)
            return render_template("index.html", uploaded_image=filepath, result_image=result_path)

    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=False)
