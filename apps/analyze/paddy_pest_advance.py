# apps/analyze/advance_paddy_pest.py

import os
import numpy as np
from PIL import Image
import tensorflow as tf
from datetime import datetime
from .models import db, ADpaddyPestAnalysisResult

# Path to the TensorFlow Lite model file
TFLITE_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modules', 'advanced_paddy_pest_model.tflite')
TEMP_FOLDER = os.path.join(os.path.dirname(__file__), 'temp_paddy_pest')

# Initialize the TensorFlow Lite interpreter
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL_PATH)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to preprocess the input image
def preprocess_image(image_path):
    input_shape = input_details[0]['shape']
    img = Image.open(image_path).convert('RGB').resize((input_shape[1], input_shape[2]))
    img = np.array(img, dtype=np.uint8)
    img = np.expand_dims(img, axis=0)
    return img

# Define a mapping from model output to disease names
PEST_CATEGORIES = {
    0: 'LEAF FOLDERS',
    1: 'WHORL MAGGOTS',
    2: 'RICE BUGS',
    3: 'STEM BORER',
    4: 'GREEN LEAFHOPPERS'
}

# Function to perform advanced paddy analysis
def advanced_paddy_pest_analysis(user_name):
    print("Performing advanced paddy analysis...")
    # Initialize counts for each disease
    disease_counts = {disease: 0 for disease in PEST_CATEGORIES.values()}

    # Process each image in the temp folder
    for filename in os.listdir(TEMP_FOLDER):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(TEMP_FOLDER, filename)
            input_data = preprocess_image(image_path)
            
            # Run inference
            interpreter.set_tensor(input_details[0]['index'], input_data)
            interpreter.invoke()
            output_data = interpreter.get_tensor(output_details[0]['index'])
            
            # Get the predicted class index
            predicted_class_index = np.argmax(output_data)
            
            # Get the disease name from the mapping
            disease_name = PEST_CATEGORIES.get(predicted_class_index, "Unknown")
            
            # Increment the count for the detected disease
            if disease_name in disease_counts:
                disease_counts[disease_name] += 1

    # Save the analysis result to the database
    analysis_date = datetime.now()
    analysis_result = ADpaddyPestAnalysisResult(
        date=analysis_date,
        user_name=user_name,
        leaf_folders_count=disease_counts.get('LEAF FOLDERS', 0),
        whorl_maggots_count=disease_counts.get('WHORL MAGGOTS', 0),
        rice_bugs_count=disease_counts.get('RICE BUGS', 0),
        stem_borer_count=disease_counts.get('STEM BORER', 0),
        green_leafhoppers_count=disease_counts.get('GREEN LEAFHOPPERS', 0),
        # Add other disease counts as necessary
    )
    db.session.add(analysis_result)
    db.session.commit()

    # Delete all images in the temp folder
    for filename in os.listdir(TEMP_FOLDER):
        file_path = os.path.join(TEMP_FOLDER, filename)
        os.remove(file_path)
    

    print("Advanced analysis complete and data saved to database.")

