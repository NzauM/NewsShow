from flask import render_template
from . import main
from ..request import get_news,get_articles

@main.route('/')
def index():
    local_news = get_news('sources')
    print(local_news)
    return render_template('index.html',sources = local_news)



@main.route('/article/<id>')
def article(id):

    article = get_articles(id)
    return render_template('article.html',article = article)