# apps/analyze/advance_paddy.py

import os
import numpy as np
from PIL import Image
import tensorflow as tf
from datetime import datetime
from .models import db, ADpaddydenalysisResult

# Path to the TensorFlow Lite model file
TFLITE_MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modules', 'advanced_paddy_model.tflite')
TEMP_FOLDER = os.path.join(os.path.dirname(__file__), 'temp_paddy_des')

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
    3: 'Bacterial panicle blight',
    8: 'Dead heart',
    4: 'Brown spot',
    6: 'Bacterial leaf streak',
    9: 'Blast',
    0: 'Tungro',
    5: 'Hispa',
    7: 'Bacterial leaf blight',
    2: 'Downy mildew',
    1: 'Leaf Smut'
}

# Function to perform advanced paddy analysis
def advanced_paddy_analysis(user_name):
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
    analysis_result = ADpaddydenalysisResult(
        date=analysis_date,
        user_name=user_name,
        # Mapping each disease count to the corresponding field in the database model
        bacterial_panicle_blight_count=disease_counts['Bacterial panicle blight'],
        dead_heart_count=disease_counts['Dead heart'],
        brown_spot_count=disease_counts['Brown spot'],
        bacterial_leaf_streak_count=disease_counts['Bacterial leaf streak'],
        blast_count=disease_counts['Blast'],
        tungro_count=disease_counts['Tungro'],
        nispa_count=disease_counts['Hispa'],
        bacterial_leaf_high_count=disease_counts['Bacterial leaf blight'],
        downy_mildew_count=disease_counts['Downy mildew'],
        leaf_smut_count=disease_counts['Leaf Smut'],
        # Add other disease counts as necessary
    )
    db.session.add(analysis_result)
    db.session.commit()

    # Delete all images in the temp folder
    for filename in os.listdir(TEMP_FOLDER):
        file_path = os.path.join(TEMP_FOLDER, filename)
        os.remove(file_path)

    print("Advanced analysis complete and data saved to database.")


    
