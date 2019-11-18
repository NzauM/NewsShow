from app import app
import urllib.request,json
from .models import news
from .models import articles



News = news.News
Articles = articles.Articles

# new2_news_url = "https://newsapi.org/v2/everything?sources={}&apiKey=38d71ea0c25f44a79c92a2e370b3316a"
# new_news_url = new2_news_url.format({{news.name}})
api_key = app.config['NEWS_API_KEY']

base_url = app.config["BASE_URL"]

def get_news(publisher):
    # get_news_url = base_url.format(apiKey)
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
        url = news_item.get('id')
        results = News(name,description,url)
        news_results.append(results)

       

    return news_results

def get_articles(source_id):
    # article_url = "https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}"
    # get_article_location_url = article_url.format(source_id,limit,api_key)
    # get_article_location_url = "https://newsapi.org/v2/everything?sources={news.name}&apiKey=38d71ea0c25f44a79c92a2e370b3316a"
    get_article_location_url1 ='https://newsapi.org/v2/everything?sources={}&apiKey=38d71ea0c25f44a79c92a2e370b3316a'
    get_article_location_url = get_article_location_url1.format(source_id)


    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_resp = json.loads(articles_location_data)

        articles_location_results = None
        if articles_location_resp['articles']:
            # id = articles_location_resp.get('id')
            # title = articles_location_resp.get('title')
            # description = articles_location_resp.get('description')
            # image = articles_location_resp.get('urlToImage')
            # publishedAt = articles_location_resp.get('publishedAt')
            # readMore = articles_location_resp.get('url')

            # articles_location_results = Articles(id,title,description,image,publishedAt,readMore)
            articles_location_list = articles_location_resp['articles']
            articles_location_results = process_articles(articles_location_list)


    return articles_location_results



#     with urllib.request.urlopen(get_article_location_url) as url:
#         articles_location_data = url.read()
#         articles_location_resp = json.loads(articles_location_data)

#         articles_location_results = None

#         if articles_location_resp['articles']:
#             articles_location_results1 = articles_location_resp['articles']
#             articles_location_results = process_articles(articles_location_results1)


#     return articles_location_results


def process_articles(my_articles):
    articles_location_list = []

    for article in my_articles:
        id = article.get('id')
        title = article.get('title')
        description = article.get('description')
        image = article.get('urlToImage')       
        publishedAt = article.get('publishedAt')
        readMore = article.get('url')

        if image:
            article_source_object = Articles(id,title,description,readMore,image,publishedAt)
            articles_location_list.append(article_source_object)

    return articles_location_list
