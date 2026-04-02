from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from werkzeug.utils import secure_filename
from model import detect_deepfake

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Run detection
        result = detect_deepfake(filepath)
        
        # Add the image url to the result so the frontend can display it
        result['image_url'] = url_for('static', filename=f'uploads/{filename}')
        
        return jsonify(result)
        
    return jsonify({'error': 'Invalid file type. Allowed: png, jpg, jpeg'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
