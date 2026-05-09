from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("doodle_model.h5")


CATEGORIES = ["Apple","Cookie","Dog","Eye","Face"]

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read())).convert("L")
    image = image.resize((28, 28))

    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    index = np.argmax(prediction)

    return jsonify({
        "prediction": CATEGORIES[index],
        "confidence": float(np.max(prediction))
    })

if __name__ == "__main__":
    app.run(debug=True)
