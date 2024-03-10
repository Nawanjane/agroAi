# apps/analyze/advance_tea.py

import os
import numpy as np
from PIL import Image
import tensorflow as tf
from datetime import datetime
from .models import db, ADvTeaAnalysisResult

# Path to the TensorFlow Lite model file
TFLITE_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modules', 'advance_tea_decies_mode.tflite')
TEMP_FOLDER = os.path.join(os.path.dirname(__file__), 'temp')

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
disease_mapping = {
    0: 'bird eye spot',
    1: 'white spot',
    2: 'Anthracnose',
    3: 'algal_leaf',
    4: 'gray_light',
    5: 'brown blight',
    6: 'red leaf spot',
}

# Function to perform advanced paddy analysis
def advanced_tea_analysis(user_name):
    print("Performing advanced paddy analysis...")
    # Initialize counts for each disease
    disease_counts = {disease: 0 for disease in disease_mapping.values()}

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
            disease_name = disease_mapping.get(predicted_class_index, "Unknown")
            
            # Increment the count for the detected disease
            if disease_name in disease_counts:
                disease_counts[disease_name] += 1

    # Save the analysis result to the database
    analysis_date = datetime.now()
    analysis_result = ADvTeaAnalysisResult(
        date=analysis_date,
        user_name=user_name,
        # Mapping each disease count to the corresponding field in the database model
        bird_eye_spot_count=disease_counts['bird eye spot'],
        white_spot_count=disease_counts['white spot'],
        Anthracnose_count=disease_counts['Anthracnose'],
        algal_leaf_count=disease_counts['algal_leaf'],
        gray_light_count=disease_counts['gray_light'],
        brown_blight_count=disease_counts['brown blight'],
        red_leaf_spot_count=disease_counts['red leaf spot'],
    
        # Add other disease counts as necessary
    )
    db.session.add(analysis_result)
    db.session.commit()

    # Delete all images in the temp folder
    for filename in os.listdir(TEMP_FOLDER):
        file_path = os.path.join(TEMP_FOLDER, filename)
        os.remove(file_path)

    print("Advanced analysis complete and data saved to database.")


    
