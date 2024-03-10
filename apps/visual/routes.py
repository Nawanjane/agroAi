# apps/visual/routes.py

from flask import Blueprint, render_template
from flask_login import login_required
from apps.visual.second_card import get_card_data
from apps.visual.first_card import get_healthy_paddy_percentage
from apps.visual.crop_yield import get_crop_yield_prediction 
from apps.visual.third_card import get_pest_percentage
from apps.visual.data_fetcher import fetch_paddy_analysis_data
import json
from .data_fetcher import fetch_paddy_pest_analysis_data
from .data_fetcher import fetch_tea_analysis_data
from .data_fetcher import paddy_advanve_pi_disease_data
from .data_fetcher import tea_advanve_pi_disease_data
from .data_fetcher import paddy_pest_advanve_pi_disease_data
from .pest_ai import generate_pest_suggestions


# Define the blueprint for the 'visual' module
blueprint = Blueprint('visual_blueprint', __name__, template_folder='templates')

@blueprint.route('/index')
@login_required
def index():
    # Get data for the card
    card_data = get_card_data()
    healthy_paddy_pre = get_healthy_paddy_percentage()
    crop_yield_prediction = get_crop_yield_prediction()
    pest_percentage = get_pest_percentage()
    #tables
    dates, healthy_counts, unhealthy_counts = fetch_paddy_analysis_data()
    
    # Convert the data to JSON strings
    data_json = json.dumps({
        'dates': dates,
        'healthy_counts': healthy_counts,
        'unhealthy_counts': unhealthy_counts
    })
    dates, without_pest_count, with_pest_count = fetch_paddy_pest_analysis_data()
    
    # Convert the data to JSON strings
    data_pest_json = json.dumps({
        'dates': dates,
        'without_pest_count': without_pest_count,
        'with_pest_count': with_pest_count
    })
    dates, healthy_counts, unhealthy_counts = fetch_tea_analysis_data()
    
    # Convert the data to JSON strings
    data_tea_json = json.dumps({
        'dates': dates,
        'healthy_counts': healthy_counts,
        'unhealthy_counts': unhealthy_counts
    })
    series_data, labels = paddy_advanve_pi_disease_data()
    
    # Convert the data to JSON strings
    data_paddy_pi_json = json.dumps({
        'series_data': series_data,
        'labels': labels,
        
    })
    series_data, labels = tea_advanve_pi_disease_data()
    
    # Convert the data to JSON strings
    data_tea_pi_json = json.dumps({
        'series_data': series_data,
        'labels': labels,
        
    })
    series_data, labels = paddy_pest_advanve_pi_disease_data()
    
    # Convert the data to JSON strings
    data_paddy_pest_pi_json = json.dumps({
        'series_data': series_data,
        'labels': labels,
        
    })
    return render_template('home/index.html', segment='index', card_data=card_data, healthy_paddy_pre=healthy_paddy_pre,crop_yield_prediction=crop_yield_prediction,pest_percentage=pest_percentage,data_json=data_json,data_pest_json=data_pest_json,data_tea_json=data_tea_json,data_paddy_pi_json=data_paddy_pi_json,data_tea_pi_json=data_tea_pi_json,data_paddy_pest_pi_json=data_paddy_pest_pi_json)

@blueprint.route('/dashboard')
def dashboard():
    user_name = "example_user"  # Replace with the actual username or logic to retrieve the username
    ai_suggestion = generate_pest_suggestions()
    return render_template('home/dashboard.html', ai_suggestion=ai_suggestion)