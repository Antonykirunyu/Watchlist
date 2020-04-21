form flask import render_temlpate
from app import app

#Views
@app.route('/')
def index():
    
     '''
     view root page function that returns the index page and its data
     '''
     return render_template('index.html')