import mongoengine
import json
import schedule
import time

from config import MONGODB
from app.db import source_dao, article_dao
from crawlerengine.source import Source


def connect_database():
    mongoengine.connect(
        MONGODB['name'], host='mongodb+srv://hailamvn123:hailamvn456@cluster0.mnwrn.mongodb.net/Newspaper?retryWrites=true&w=majority')


def source_job(src_data):
    config = src_data['config']
    source_crawler = Source(
        url=src_data['url'], config=config, lang=src_data['language'])
    source_crawler.set_all_articles()
    for article_crawler in source_crawler.articles:
        ar_data = {
            'url': article_crawler.url,
            'source_url': src_data['url'],
            'author': article_crawler.author,
            'publish_date': article_crawler.publish_date,
            'title': article_crawler.title,
            'content': article_crawler.content,
            'categories': article_crawler.category,
            'tags': article_crawler.tags
        }
        adao = article_dao.ArticleDAO(ar_data)

        for cate in article_crawler.category:
            adao.save_category(cate)

        for tag in article_crawler.tags:
            adao.save_article_tag(tag)

        adao.save_an_article()


if __name__ == '__main__':
    connect_database()
    t = source_dao.SourceDAO()
    sources = t.get_all_sources()

    for src in sources:
        src_data = json.loads(src)
        for hour in src_data['schedule']:
            print(hour)
            schedule.every().day.at(str(hour)).do(source_job, src_data=src_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # print(Sources.objects)
