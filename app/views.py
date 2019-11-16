from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    local_news = get_news('sources')
    print(local_news)
    return render_template('index.html',sources = local_news)

@app.route('/news/<news_source>')
def news(news_source):
    return render_template('news.html',source = news_source)