
# 🎨 Doodle Recognition: 5-Class CNN

An interactive deep learning application that recognizes hand-drawn doodles in real-time. Built using a **Convolutional Neural Network (CNN)** and trained on a subset of Google’s "Quick, Draw!" dataset.

## 🚀 Overview

This project classifies sketches into five distinct categories. Users can draw directly on a digital canvas, and the model predicts what is being drawn using computer vision techniques.

### Selected Categories:

*  **Apple**
*  **Cookie**
*  **Dog**
*  **Eye**
*  **Face**
*(Note: You can swap these out in your training script.)*

---

## 🧠 Model Architecture

The core of this project is a **Convolutional Neural Network (CNN)**. CNNs are specifically designed for spatial hierarchy in data, making them perfect for recognizing patterns in brush strokes.

The model follows this general structure:

1. **Input Layer:** Gray-scale images (usually  pixels).
2. **Convolutional Layers:** To extract features like edges and curves.
3. **Pooling Layers:** To reduce dimensionality and computational load.
4. **Dense (Fully Connected) Layers:** To classify the features into one of the 5 categories.
5. **Softmax Output:** To provide a probability score for each class.

---

## 🛠️ Tech Stack

* **Deep Learning:** TensorFlow / Keras
* **Data Processing:** NumPy, Pandas, OpenCV
* **Frontend/Canvas:** [Streamlit / Flask / Tkinter] *(Choose your implementation)*
* **Dataset:** [Google Quick, Draw! Dataset](https://github.com/googlecreativelab/quickdraw-dataset)

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aKmsdfhjb/Doodle.git
cd doodle

```

### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. Run the application

```bash
python app.py

```

---

## 📊 Dataset & Training

The model was trained on ** grayscale bitmap files** (.npy format).

* **Data Augmentation:** Used to improve model robustness against different drawing styles.
* **Optimizer:** Adam
* **Loss Function:** Categorical Crossentropy

| Metric | Score |
| --- | --- |

| **Validation Accuracy** | ~96% |

---

## 🖼️ Preview

> Loading...

---

## 🤝 Contributing

Feel free to fork this project, add more categories, or optimize the CNN layers. Pull requests are always welcome!

---

