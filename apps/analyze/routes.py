# apps/analyze/routes.py

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from .tea import run_tea_analysis
from .paddy import run_paddy_analysis
from .paddy_pest import run_paddy_pest_analysis
import os

blueprint = Blueprint('analyze', __name__, template_folder='templates')
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'upload', 'files')

@blueprint.route('/analyze', methods=['GET', 'POST'])
def analyze():
    folders = next(os.walk(UPLOAD_FOLDER))[1]
    
    if request.method == 'POST':
        selected_folder = request.form.get('selected_folder')
        analysis_mode = request.form.get('analysis_mode')
        folder_path = os.path.join(UPLOAD_FOLDER, selected_folder)

        # Ensure the user is logged in
        if not current_user.is_authenticated:
            flash('Please log in to perform analysis.')
            return redirect(url_for('authentication_blueprint.login'))  # Replace 'auth.login' with your actual login view

        # Get the username from the current_user proxy
        user_name = current_user.username
        
        if analysis_mode == 'tea':
            run_tea_analysis(folder_path, user_name)
            flash(f'Tea analysis complete for {selected_folder}.')
        elif analysis_mode == 'paddy_decies':
            run_paddy_analysis(folder_path, user_name) 
            flash(f'Paddy analysis complete for {selected_folder}.')
        elif analysis_mode == 'paddy_pest': 
            run_paddy_pest_analysis(folder_path, user_name)
            flash(f'Paddy analysis complete for {selected_folder}.')    
        
        return redirect(url_for('analyze.analyze'))

    return render_template('analyze.html', folders=folders)

