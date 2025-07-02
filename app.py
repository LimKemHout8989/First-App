from flask import Flask , render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')


@app.route('/apply')
def apply():
  return render_template('apply.html')


# Upload configuration
app.config['UPLOAD_FOLDER'] = 'folder_upload'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/submit', methods=['POST'])
def submit():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    resume = request.files['resume']

    filename = name +"__"+ secure_filename(resume.filename)
    resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('submit_seccesful.html')


if __name__ == '__main__':
  app.run(host = '0.0.0.0',debug=True)
