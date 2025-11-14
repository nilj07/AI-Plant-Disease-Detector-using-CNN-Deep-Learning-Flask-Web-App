from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load model
MODEL_PATH = 'model/plant_disease_cnn_model.h5'
model = load_model(MODEL_PATH)

# Class labels (same order as training)
class_labels = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

idx_to_class = {i: label for i, label in enumerate(class_labels)}

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file found"}), 400

        file = request.files["file"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Load & preprocess image
        img = image.load_img(filepath, target_size=(160,160))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0) / 255.0

        pred = model.predict(img)
        idx = np.argmax(pred)
        confidence = float(pred[0][idx])

        label = idx_to_class[idx]

        if confidence < 0.5:
            return jsonify({
                "status": "low_confidence",
                "message": "Cannot detect disease. Please upload a clearer image.",
                "confidence": f"{confidence*100:.2f}%"
            })

        return jsonify({
            "status": "success",
            "predicted_class": label,
            "confidence": f"{confidence*100:.2f}%"
        })

    except Exception as e:
        print("🔥 SERVER ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
