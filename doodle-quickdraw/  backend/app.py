from pathlib import Path
import os
import io

from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
from PIL import Image
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "doodle_model.h5"
CATEGORIES = ["Apple", "Cookie", "Dog", "Eye", "Face"]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
origins = [
    item.strip()
    for item in os.getenv(
        "CORS_ORIGINS",
        "https://aKmsdfhjb.github.io,http://localhost:8000,http://127.0.0.1:8000",
    ).split(",")
    if item.strip()
]
CORS(app, resources={r"/predict": {"origins": origins}, r"/health": {"origins": origins}})

model = None
model_error = None
try:
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as exc:
    model_error = str(exc)


@app.get("/health")
def health():
    return jsonify({"ready": model is not None, "error": model_error})


@app.post("/predict")
def predict():
    if model is None:
        return jsonify({"error": "Model is unavailable. Check the model file and backend logs."}), 503

    uploaded = request.files.get("image")
    if uploaded is None:
        return jsonify({"error": "Upload a drawing in the image field."}), 400

    try:
        image = Image.open(io.BytesIO(uploaded.read())).convert("L")
        image = image.resize((28, 28))
        image_array = np.asarray(image, dtype=np.float32) / 255.0
        image_array = image_array.reshape(1, 28, 28, 1)
        scores = model.predict(image_array, verbose=0)[0]
        if len(scores) != len(CATEGORIES):
            return jsonify({"error": "Model output does not match the five configured classes."}), 500
        index = int(np.argmax(scores))
        return jsonify({
            "prediction": CATEGORIES[index],
            "confidence": float(scores[index]),
        })
    except Exception:
        app.logger.exception("Could not process drawing")
        return jsonify({"error": "The drawing could not be processed."}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
