from flask import render_template
from . import main
from ..request import get_news,get_articles

@main.route('/')
def index():
    local_news = get_news('sources')
    print(local_news)
    return render_template('index.html',sources = local_news)

# @app.route('/news/<name>')
# def newsStories(sources):

#     story = get_newsStories(sources)
#     return render_template('story.html',story=newsStories)

# 


@main.route('/article/<id>')
def article(id):

    article = get_articles(id)
    # title = f'{{article.title}}'
    return render_template('article.html',article = article)