# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.visual.second_card import get_card_data
from apps.visual.first_card import get_healthy_paddy_percentage
from apps.visual.crop_yield import get_crop_yield_prediction 
from apps.visual.third_card import get_pest_percentage
from apps.visual.data_fetcher import fetch_paddy_analysis_data
import json
from apps.visual.data_fetcher import fetch_paddy_pest_analysis_data
from apps.visual.data_fetcher import fetch_tea_analysis_data
from apps.visual.data_fetcher import paddy_advanve_pi_disease_data
from apps.visual.data_fetcher import tea_advanve_pi_disease_data
from apps.visual.data_fetcher import paddy_pest_advanve_pi_disease_data
from apps.visual.pest_ai import generate_pest_suggestions



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

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None


