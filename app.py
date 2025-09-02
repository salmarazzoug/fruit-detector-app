from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    image_path = 'uploaded.jpg'
    file.save(image_path)

    result = subprocess.check_output(['python', 'detect.py', image_path])
    return result

if __name__ == '__main__':
    app.run(debug=True)
