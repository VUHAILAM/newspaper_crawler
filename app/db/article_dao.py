from datetime import date
from newspaper import article, source
from .models import Article, ArticleTag, Category, Sources

class ArticleDAO(object):
    def __init__(self, data) -> None:
        self.article = Article()
        self.data = data

    def save_category(self, data):
        check_cate = Category.objects(category=data).first()
        if check_cate is not None:
            return
        category = Category(category=data)
        category.save()

    def save_article_tag(self, data):
        check_tag = ArticleTag.objects(tag=data).first()
        if check_tag is not None:
            return
        article_tag = ArticleTag(tag=data)
        article_tag.save()

    def save_an_article(self):
        check_aritcle = Article.objects(url=self.data['url']).first()
        if check_aritcle is not None:
            return

        article = Article()
        article.url = self.data['url']
        article.title = self.data['title']
        article.author = self.data['author']
        article.publish_date = self.data['publish_date']
        article.content = self.data['content']

        source = Sources.objects(url = self.data['source_url']).first()
        article.source = source

        for cate in self.data['categories']:
            category = Category.objects(category=cate).first()
            article.categories.append(category)
        
        for tag in self.data['tags']:
            article_tag = ArticleTag.objects(tag=tag).first()
            article.tag.append(article_tag)
        
        article.save()

