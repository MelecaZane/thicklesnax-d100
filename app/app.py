from flask import render_template, request, redirect, url_for, flash, Flask
from werkzeug.utils import secure_filename
import os
import functions

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

flask_app = Flask(__name__, static_url_path='/static')
flask_app.secret_key = os.environ.get('FLASK_SECRET_KEY')
flask_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/table')
def table():
    filename = request.args.get('file')
    try:
        return render_template('table.html',
                               data=functions.parse_csv(os.path.join(flask_app.config['UPLOAD_FOLDER'], filename)))
    except:
        return redirect(url_for('home'))

@flask_app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and functions.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(flask_app.config['UPLOAD_FOLDER'], filename))
        flash('File uploaded successfully')
        return redirect(url_for('table', file=filename))
    return redirect(url_for('home'))