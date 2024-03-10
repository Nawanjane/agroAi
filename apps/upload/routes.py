# apps/upload/routes.py

import os
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

blueprint = Blueprint('upload', __name__, template_folder='templates')

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@blueprint.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('files')
        subfolder_name = request.form.get('subfolder_name', '')

        if not files or len(files) == 0:
            flash('No files selected')
            return redirect(request.url)

        if len(files) > 100:
            flash('You cannot upload more than 100 files at a time')
            return redirect(request.url)

        subfolder_path = os.path.join(UPLOAD_FOLDER, secure_filename(subfolder_name))
        os.makedirs(subfolder_path, exist_ok=True)

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(subfolder_path, filename))

        flash(f'{len(files)} files successfully uploaded')
        return redirect(url_for('upload.upload_files'))

    return render_template('upload.html')