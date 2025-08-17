# 🍎🍊 YOLOv8 Object Detection: Apples vs Oranges  

![Demo GIF]([demo.gif](https://github.com/younes-damouna/object-detection-yolo-v8/blob/main/static/demo.gif)) <!-- replace with your actual GIF or screenshot -->

---

## 📌 Project Overview  
This project demonstrates the deployment of a **YOLOv8 object detection model** using **Flask** and **Docker**.  

The model is trained to **differentiate between apples and oranges** by drawing bounding boxes around each fruit in an uploaded image.  

Users can upload an image through a simple **web interface**, and the app returns the same image annotated with detection results.  

---

## 🚀 Features  
- ✅ **YOLOv8 Model** trained for fruit classification *(apples vs oranges)*  
- ✅ **Web-based interface (Flask)** for image upload & prediction  
- ✅ **Bounding boxes** drawn on detected fruits  
- ✅ **Dockerized application** for easy deployment  
- ✅ Deployable to **Render** or any Docker-compatible cloud service  

---

## 🛠️ Local Setup Instructions  

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/younes-damouna/object-detection-yolo-v8.git
cd object-detection-yolo-v8

```
### 2️⃣ Create Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```

### 4️⃣ Run Flask App
```bash
python app.py

```
### 5️⃣ Access the App
Open your browser at 👉 http://localhost:5000

----------------------

## 🐳 Run with Docker  

### Build the Image
```bash
docker build -t object-detection-yolo-v8 .
```
### Run the Container

```bash
docker run -p 5000:5000 object-detection-yolo-v8
```
Now visit 👉 http://localhost:5000

------

### 🌐 Online Deployment (Render Example)

Create a Render Account → https://render.com

New Web Service → Connect your GitHub repo

complete the setup

Your app will be live at: → https://object-detection-yolo-v8.onrender.com/

----

### 🖥️ Usage

1. Upload an image containing apples and/or oranges.

2. Wait a few seconds while the model processes the image.

3. View the annotated image with bounding boxes showing detected fruits.


----
### 📂 Project Structure

```bash
app/
├── models/ # YOLOv8 trained weights (best.pt)
├── static/ # Uploaded images & detection results
├── templates/ # HTML template (Flask UI)
├── app.py # Flask backend
├── requirements.txt # Python dependencies
└── Dockerfile # For containerization
```
-----
### ⚠️ Known Issues / Limitations

- 🕒 Inference speed may be slower on CPU-only deployment.

- 📷 Works best on clear, well-lit images of fruits.

- 📦 Current version only supports apples and oranges (but extendable).

- 🔧 Large images may take longer to process (consider resizing before upload).

----


### 🌐 Live Demo

Deployed app (Render): https://object-detection-yolo-v8.onrender.com/

----

### ✨ If you like this project, consider giving it a ⭐ on GitHub!
