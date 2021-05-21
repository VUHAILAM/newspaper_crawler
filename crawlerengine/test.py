import datetime

#from crawlerengine.source import Source
import newspaper
from source import Source
from article import Article
#a = Article('https://vnexpress.net/vega-city-nha-trang-ra-mat-chuoi-shophouse-trung-tam-du-an-4276270.html')

#a.extract_tags(list_tag_name='div' ,list_class_name='tags', tag_name='h4', tag_class_name='item-tag')
if __name__ == '__main__':
    s = newspaper.build('https://vtc.vn/', memoize_articles=False)
    #s = Source('https://dantri.com.vn/', lang= 'vi')
    #s.get_articles_by_date(datetime.date.today())
    tr = s.article_urls()
    print(len(tr))