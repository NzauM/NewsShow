from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    This is a view function that will return contents of the index page
    '''
    return render_template('index.html')

@app.route('/news/<publisher>')
def news(publisher):
    '''
    Returns some news company page containingits data
    '''
    return render_template('publisher.html'publisher = publisher)


