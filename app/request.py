from app import app
import urllib.request,json
from .models import news
from .models import story



News = news.News
# api_key = app.config['NEWS_API_KEY']

# base_url = app.config["BASE_URL"]

def get_news(publisher):
    # get_news_url = base_url.format(publisher,apiKey)
    get_news_url = "https://newsapi.org/v2/sources?&apiKey=38d71ea0c25f44a79c92a2e370b3316a"

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_resp = json.loads(get_news_data)

        news_results = None

        if get_news_resp['sources']:
            news_results_list = get_news_resp['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        results = News(name,description,url)
        news_results.append(results)

       

    return news_results

def get_newsStories(name):
    get_news_stories = "https://newsapi.org/v2/everything?sources={}&apiKey=38d71ea0c25f44a79c92a2e370b3316a"
    get_news_stories_Url = get_news_stories.format(sources)

    with urllib.request.urlopen(get_news_stories_Url) as url:
        stories_data = url.read()
        stories_data_resp = json.loads(stories_data)

        news_story = None
        if stories_data_resp:
            author = stories_data_resp.get('author')
            title = stories_data_resp.get('title')
            description = stories_data_resp('description')
            image = stories_data_resp.get('urlToImage')
            publishedAt = stories_data_resp.get('publishedAt')
            readMore = stories_data_resp.get('url')

            news_story = Story(author,title,description,image,publishedAt,readMore)

    return news_story

