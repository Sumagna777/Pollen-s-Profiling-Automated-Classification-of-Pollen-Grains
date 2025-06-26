from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model("model.h5")

# ✅ Actual class names from your dataset
classes = ['anadenanthera', 'arecaceae', 'arrabidaea', 'cecropia', 'chromolaena', 'combretum', 'croton', 'dipteryx',
           'eucalipto', 'faramea', 'hyptis', 'mabea', 'matayba', 'mimosa', 'myrcia', 'protium', 'qualea', 'schinus',
           'senegalia', 'serjania', 'syagrus', 'tridax', 'urochloa']

# ✅ Make sure this folder exists: static/uploads/
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction.html')
def predict_page():
    return render_template('prediction.html')

@app.route('/logout.html')
def logout():
    return render_template('logout.html')

@app.route('/result', methods=['POST'])
def result():
    if 'image' not in request.files:
        return "No file uploaded."

    f = request.files['image']
    if f.filename == '':
        return "No file selected."

    # Save to static/uploads folder
    image_path = os.path.join(UPLOAD_FOLDER, 'uploaded_image.jpg')
    f.save(image_path)

    # Preprocess
    img = image.load_img(image_path, target_size=(128, 128))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # Predict
    prediction = model.predict(x)
    class_index = np.argmax(prediction[0])
    class_label = classes[class_index]
    confidence = round(np.max(prediction[0]) * 100, 2)

    result_text = f'Predicted Class: {class_label} ({confidence}%)'
    return render_template('prediction.html', result=result_text, image_file='uploads/uploaded_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)
