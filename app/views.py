from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    local_news = get_news('sources')
    print(local_news)
    return render_template('index.html',sources = local_news)

# @app.route('/news/<name>')
# def newsStories(sources):

#     story = get_newsStories(sources)
#     return render_template('story.html',story=newsStories)