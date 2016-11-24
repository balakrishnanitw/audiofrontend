# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
from flask import jsonify
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "C:\\Workspace\\Emotion-Recognition\\t\\src\\audio"
app.config['ALLOWED_EXTENSIONS'] = set(['wav'])
def join():
    return ''.join(['Recognised','Emotion ','in the audio file ','is ','angry'])
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")
                       
    
@app.route('/upload', methods=['POST','GET'])
def upload():
    x=join()
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))        
        return jsonify(x) #render_template('complete.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
@app.route('/<filename>')
def song(filename):
    return render_template('play.html',
                        title = filename,
                        music_file = filename)                               


port = os.getenv('PORT', '8000')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port),debug = True)
