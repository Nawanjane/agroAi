# apps/analyze/paddy_pest.py

import os
import shutil
from PIL import Image
import numpy as np
import tensorflow as tf
from datetime import datetime
from .models import db, paddyPestAnalysisResult
from .paddy_pest_advance import advanced_paddy_pest_analysis

# Path to the TensorFlow Lite model file
TFLITE_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modules', 'paddy_pest_detect.tflite')
TEMP_FOLDER = os.path.join(os.path.dirname(__file__), 'temp_paddy_pest')

# Initialize the TensorFlow Lite interpreter
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image_path):
    input_shape = input_details[0]['shape']
    img = Image.open(image_path).convert('RGB')
    img = img.resize((input_shape[1], input_shape[2]))
    img = np.array(img, dtype=np.uint8)
    img = np.expand_dims(img, axis=0)
    return img

def count_images_in_folder(folder_path):
    image_count = sum(1 for filename in os.listdir(folder_path) if filename.lower().endswith(('.png', '.jpg', '.jpeg')))
    return image_count

def run_paddy_pest_analysis(folder_path, user_name):
    analysis_results = []  # List to store tuples of (output, image_path)

    # Ensure temp folder exists
    os.makedirs(TEMP_FOLDER, exist_ok=True)

    # Process each image in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            input_data = preprocess_image(image_path)
            
            # Run inference
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            
            # Assuming the model returns a single output with 0 for without pest and 1 for with pest
            predicted_class = np.argmax(output_data)  # Get the predicted class index
            analysis_results.append((predicted_class, image_path))

    
    # Copy the images with pests to the temp folder and store their paths
    for result, image_path in analysis_results:
        if result == 1:
            filename = os.path.basename(image_path)
            temp_image_path = os.path.join(TEMP_FOLDER, filename)
            shutil.copy(image_path, temp_image_path)
# Count the number of files with and without pests
    with_pest_count = count_images_in_folder(TEMP_FOLDER)
    without_pest_count = count_images_in_folder(folder_path)-count_images_in_folder(TEMP_FOLDER)
    # Save the analysis result to the database
    analysis_date = datetime.now()
    analysis_result = paddyPestAnalysisResult(
        date=analysis_date,
        user_name=user_name,
        with_pest_count=with_pest_count,
        without_pest_count=without_pest_count
    )
    db.session.add(analysis_result)
    db.session.commit()

    advanced_analysis_results = advanced_paddy_pest_analysis(user_name)
    return with_pest_count, without_pest_count,advanced_analysis_results
