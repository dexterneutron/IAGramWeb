from flask import Flask,request,redirect,render_template
from imagemaker import AllImages
from db import InsertOutput,GetFinalImages,DeleteAllOutput
from imageLoader import DeleteAllImages
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    try:
            ilist=GetFinalImages()
            return render_template('index.html',ilist=ilist)
    except:
            return 'No pude generar las imagenes elmikiti'
 
@app.route('/maker')
def maker():
    try:
            AllImages()
            #InsertOutput()
            return redirect('/')

    except:
            return 'No pude generar las imagenes elmikiti'


@app.route('/deleteall')
def deleteall():
    
    try:
            DeleteAllOutput()
            #DeletAllImages()
            #InsertOutput()
            return redirect('/')
    except:
            return 'No pude borrar las mmgvada yave'
 
@app.route('/refreshall')
def refreshall():
    
    try:
            DeleteAllOutput()
            AllImages()
            #DeletAllImages()
            #InsertOutput()
            return redirect('/')
    except:
            return 'No pude borrar las mmgvada yave'




if __name__ == "__main__":
    app.run(debug=True)

