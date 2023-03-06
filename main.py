import datetime
import os

from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException

import database

URL = os.getenv('NEWSAPI_URL')
PAGE = 1
LIMIT = 2

def get_news_data(api_key):
    """
    Connects to the NewsAPI.org news API and returns the most popular news from the previous day.

    :param api_key: The API key to use for the NewsAPI.org API.
    :return: A list of dictionaries containing the most popular news from the previous day.
    """
    newsapi = NewsApiClient(api_key=api_key)
    last_day = datetime.date.today() - datetime.timedelta(days=1)
    try:
        most_popular_news = newsapi.get_everything(
            q='kjasksj',
            from_param=last_day,
            page=PAGE,
            page_size=LIMIT)
        if most_popular_news.get("status") == 'ok' and most_popular_news.get("totalResults") > 0:
            articles = most_popular_news.get("articles","")
        else:
            return "There no data in reponse to save in local DB"
    except (ValueError, NewsAPIException) as e:
        print(e.args)
    else:
        create_news(news=articles)


def create_news(news, connection=None):
    """
    Inserts the given news articles into the specified MySQL database.

    :param news: A list of dictionaries containing news articles.
    :param connection: The connection to the MySQL database.
    """
    try:
        database.create_table()
        database.insert_data(news)
    except Exception as e:
        print(e.args)
    else:
        print("News were inserted to database correctly!")


if __name__ == '__main__':
    api_key = os.getenv('NEWSAPI_API_KEY')
    get_news_data(api_key)
    database.close_connection()
