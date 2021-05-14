import newspaper
import datetime
import json

from .article import Article

class Source(object):
    def __init__(self, url, config, lang = ''):
        self.url = url
        self.language = lang
        self.source = newspaper.build(url=url, language=lang, memoize_articles = False)
        self.articles = []
        self.config = config
    
    def get_articles_by_date(self, date_p):
        print(self.source.size())
        articles_by_date = []
        for article_url in self.source.article_urls():
            try:
                ar = Article(article_url, self.config)
                ar.build()
                if ar.publish_date >= date_p:
                    articles_by_date.append(ar)
            except:
                print("can not get article")
        
        return articles_by_date
        
    def set_all_articles(self):
        for article_url in self.source.article_urls():
            try:
                print(article_url)
                ar = Article(article_url, self.config)
                ar.build()
                self.articles.append(ar)
            except:
                print("can not get article")
