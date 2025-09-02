```markdown
# 🍎 Fruit Detector App

## Project Overview
This project is a **Fruit Detection and Instance Segmentation** application using **Roboflow** and **YOLOv8**.  
Users can upload an image of fruits, and the app will detect and classify them with confidence scores.

- Dataset: [Fruits 1608 Dataset](https://app.roboflow.com/ds/oIDDdLpuPI?key=huQnrsqtWt)
- Model: YOLOv8 trained on Roboflow  
- Deployment: Web app using **Flask** + **HTML/JavaScript**  
- API: Roboflow API is used to make predictions after training

---

## Project Structure

```

fruit-detector-app/
│── detect.py           # Python script to call Roboflow API and predict
│── app.py              # Flask web server
│── templates/
│    └── index.html     # Web interface
│── static/
│    └── style.css      # CSS styles
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation



## Installation

1. Clone the repository:
````bash
git clone https://github.com/salmarazzoug/fruit-detector-app.git
cd fruit-detector-app
````

2. Install dependencies (recommended in a virtual environment):

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Flask Web App

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

### Upload an Image

* Click **Choose File** to select an image
* Click **Détecter**
* Results will show detected fruits and confidence scores

---

## Dataset

* Fruits 1608 Dataset
* Annotated Fruits Dataset ([Download here](https://app.roboflow.com/ds/oIDDdLpuPI?key=huQnrsqtWt))
* Subset of classes used: Apple, Banana, Orange, Strawberry, etc.

---

## Roboflow API

* Workspace: `zineb-lcfgm`
* Project: `fruites-82sjk`
* Model Version: `11`
* API Key:“Put your API key here after training the model in Roboflow with the provided dataset.”

---

## License

This project uses the Fruits 1608 dataset, which is free for educational purposes.
Feel free to use, modify, and share for learning and demo purposes.

