from flask import Flask, render_template, request, send_from_directory
from flask import Response
from werkzeug import secure_filename
import os
from pyautogui  import pymsgbox 
from psidialogs import message
from MainProject import predict


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "C:\\Workspace\\Emotion-Recognition\\t\\src\\static\\music"
app.config['ALLOWED_EXTENSIONS'] = set(['wav']) 
   
def join():
    return ''.join(['File ','uploaded ','Successfully'])
def add():
    return join()    
# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET','POST'])
def index():
    songs = os.listdir('static/music')
    return render_template("index.html",songs=songs)
                       
    
@app.route('/upload', methods=['POST','GET'])
 #render_template('complete.html')
def upload():
    
    x=join()
    src_dir =  'C:\\Workspace\\Emotion-Recognition\\t\\src\\static\\music'   
    filelist = [ f for f in os.listdir(src_dir) ]
    for f in filelist:
        os.remove(src_dir+'\\'+ f)  
    file = request.files['file']
    if file and allowed_file(file.filename):
       filename = secure_filename(file.filename)
       file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       return ('',204)
   
      

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
@app.route('/music',methods=['POST','GET'])
def music():
    y=predict()
    return pymsgbox.alert(y,"Distribustion of Emotions")                             

port = os.getenv('PORT', '8000')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port),debug = True)
     
