# Doodle Recognition — 5-Class CNN

An interactive sketch-recognition project built around a CNN trained on five Google Quick, Draw! categories: Apple, Cookie, Dog, Eye and Face.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/Model-TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-Vanilla%20JS-f0db4f?style=flat-square)

## Live frontend

The canvas interface can be published independently on GitHub Pages:

[Open Doodle Recognition](https://aKmsdfhjb.github.io/Doodle/)

GitHub Pages hosts only the browser interface. For real predictions, run or deploy the Flask/TensorFlow API and enter its URL in the frontend's **Backend API URL** field.

## Features

- Pointer- and touch-friendly drawing canvas.
- Clear and submit controls.
- Configurable API endpoint for local or hosted inference.
- Loading, connection and error states.
- Five-class prediction response with confidence score.
- Responsive ivory editorial interface.

## Architecture

~~~mermaid
flowchart TD
 A[Quick Draw dataset] --> B[Data preparation]
 B --> C[CNN training notebook]
 C --> D[Saved doodle_model.h5]
 E[Canvas frontend] --> F[PNG upload]
 F --> G[Flask prediction API]
 D --> G
 G --> H[Grayscale and resize to 28x28]
 H --> I[CNN inference]
 I --> J[Class and confidence]
 J --> E
~~~

## Run the backend locally

Use Python 3.10 and install the backend dependencies:

~~~bash
cd "doodle-quickdraw/  backend"
pip install -r requirements.txt
python app.py
~~~

The API starts on http://127.0.0.1:5000. The model file must be present beside app.py.

## Frontend

Open doodle-quickdraw/frontend/index.html locally, or use the GitHub Pages link. For local testing, set the API URL to:

~~~text
http://127.0.0.1:5000
~~~

## Project structure

- data/data_set_getter.py — dataset preparation utility.
- src/CNN Doodle.ipynb — training notebook.
- doodle-quickdraw/  backend/ — Flask inference API, dependencies and model artifact.
- doodle-quickdraw/frontend/ — static browser client.
- .github/workflows/pages.yml — GitHub Pages deployment.

## Limitations

The classifier recognizes only the five training categories. Confidence is the model's softmax score, not a guarantee of correctness. Results depend on matching the training-time image preprocessing.

## License

See the repository's license and dataset terms before redistributing trained weights or source data.


## Project Wiki

- [Wiki home](docs/wiki/Home.md)
- [Architecture and deployment](docs/wiki/Architecture.md)

The repository keeps a version-controlled wiki source under `docs/wiki/`.