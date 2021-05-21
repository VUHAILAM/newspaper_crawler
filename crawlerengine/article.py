import re
import datetime

import newspaper
from bs4 import BeautifulSoup


class Article(object):
    def __init__(self, url, config=None):
        article = newspaper.Article(url)
        article.download()
        article.parse()
        self.url = article.url
        self.title = article.title
        self.content = article.text
        self.html = article.html
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.tags = []
        self.category = []
        self.publish_date = datetime.date.today()
        self.author = ''
        self.config = config

    def extract_publish_date(self, tag_name, class_name):
        publish_date_tag = self.soup.find(tag_name, {'class': class_name})
        if publish_date_tag is None:
            return

        date_d = re.search(
            '(\d{1,4})[.\-\/](\d{1,2})[.\-\/](\d{1,4})', publish_date_tag.text)
        if date_d is None:
            return
            
        day = date_d.group(1)
        month = date_d.group(2)
        year = date_d.group(3)
        self.publish_date = datetime.date(int(year), int(month), int(day))
        print(self.publish_date)

    def extract_tags(self, list_tag_name, list_class_name, tag_name, tag_class_name):
        list_tags_tag = self.soup.find(
            list_tag_name, {'class': list_class_name})

        tags_soup = BeautifulSoup(str(list_tags_tag), 'lxml')
        tags = tags_soup.find_all(tag_name, {'class': tag_class_name})

        for t in tags:
            self.tags.append(t.text)

        print(self.tags)

    def extract_categories(self, list_tag_name, list_class_name, category_name, category_class_name):
        category_list_tag = self.soup.find(
            list_tag_name, {'class': list_class_name})
        category_soup = BeautifulSoup(str(category_list_tag), 'lxml')
        categories = category_soup.find_all(
            category_name, {'class': category_class_name})

        for c in categories:
            self.category.append(c.text)

        print(self.category)

    def extract_author(self, author_tag_name, author_class_name):
        author_tag = self.soup.find(
            author_tag_name, {'class': author_class_name})
        if author_tag is None:
            return
        self.author = author_tag.text

        print(self.author)

    def build(self):
        self.extract_publish_date(
            self.config['publish_date']['tag_name'], self.config['publish_date']['class_name'])
        self.extract_categories(self.config['categories']['tag_name'], self.config['categories']
                                ['class_name'], self.config['category']['tag_name'], self.config['category']['class_name'])
        self.extract_tags(self.config['tags']['tag_name'], self.config['tags']
                          ['class_name'], self.config['tag']['tag_name'], self.config['tag']['class_name'])
        #self.extract_author(
        #    self.config['author']['tag_name'], self.config['author']['class_name'])
