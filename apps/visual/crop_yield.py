# apps/visual/crop_yield.py
import os

import numpy as np
import tensorflow as tf
from apps.analyze.models import db, paddydenalysisResult, paddyPestAnalysisResult


current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path= os.path.join(current_dir, 'linear_regression_model.tflite'))
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to make predictions using the TensorFlow Lite model
def predict(input_data):
    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Run inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])

    return output_data

# Function to get the latest analysis results and make a crop yield prediction
def get_crop_yield_prediction():
    # Fetch the latest PaddyAnalysisResult and PaddyPestAnalysisResult entries
    latest_disease_result = paddydenalysisResult.query.order_by(paddydenalysisResult.date.desc()).first()
    latest_pest_result = paddyPestAnalysisResult.query.order_by(paddyPestAnalysisResult.date.desc()).first()

    if latest_disease_result and latest_pest_result:
        # Calculate the percentage of disease and pest presence
        total_disease = latest_disease_result.healthy_count + latest_disease_result.unhealthy_count
        disease_percentage = (latest_disease_result.unhealthy_count / total_disease) if total_disease > 0 else 0

        total_pest = latest_pest_result.without_pest_count + latest_pest_result.with_pest_count
        pest_percentage = (latest_pest_result.with_pest_count / total_pest) if total_pest > 0 else 0

        # Prepare input data for prediction
        input_data = np.array([[disease_percentage, pest_percentage]], dtype=np.float32)

        # Make prediction
        predicted_value = predict(input_data)

        # Return the predicted crop yield percentage
        return predicted_value[0][0] * 100  # Convert to percentage
    else:
        return 0  # Return 0 if there are no results

# Make sure to update the import paths and model paths based on your project structure.
