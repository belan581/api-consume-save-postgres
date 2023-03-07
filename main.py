import datetime
import os

from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
from schema import ArticlesSchema

import database

PAGE = 1
LIMIT = 2

def get_news_data(api_key):
    newsapi = NewsApiClient(api_key=api_key)
    last_day = datetime.date.today() - datetime.timedelta(days=1)
    schema = ArticlesSchema(many=True)
    try:
        most_popular_news = newsapi.get_everything(
            q='python',
            from_param=last_day,
            page=PAGE,
            page_size=LIMIT)
        if most_popular_news.get("status") == 'ok' and most_popular_news.get("totalResults") > 0:
            articles = most_popular_news.get("articles","")
            articles = schema.load(articles)
        else:
            return "There no data in reponse to save in local DB"
    except (ValueError, NewsAPIException) as e:
        print(e.args)
    else:
        create_news(news=articles)


def create_news(news, connection=None):
    try:
        database.create_table()
        database.insert_data(news)
    except Exception as e:
        print(e.args)
    else:
        print("News were inserted to database correctly!")

def run():
    api_key = os.getenv('NEWSAPI_API_KEY')
    get_news_data(api_key)
    database.close_connection()

if __name__ == '__main__':
    run()
