from mongoengine import Document, EmbeddedDocument, fields


class HTMLTag(EmbeddedDocument):
    tag_name = fields.StringField()
    class_name = fields.StringField()


class ListTypeHTMLTag(EmbeddedDocument):
    list_tag = fields.EmbeddedDocumentField(HTMLTag)
    element_tag = fields.EmbeddedDocumentField(HTMLTag)


class ConfigSource(EmbeddedDocument):
    publish_date = fields.EmbeddedDocumentField(HTMLTag)
    author = fields.EmbeddedDocumentField(HTMLTag)
    categories = fields.EmbeddedDocumentField(HTMLTag)
    category = fields.EmbeddedDocumentField(HTMLTag)
    tags = fields.EmbeddedDocumentField(HTMLTag)
    tag = fields.EmbeddedDocumentField(HTMLTag)


class Sources(Document):
    url = fields.URLField(required=True, unique=True)
    language = fields.StringField()
    config = fields.EmbeddedDocumentField(ConfigSource)
    schedule = fields.ListField(fields.StringField())
    meta = {'collection': 'Sources'}


class ArticleTag(Document):
    tag = fields.StringField(unique=True)
    meta = {'collection': 'ArticleTags'}


class Category(Document):
    category = fields.StringField(unique=True)
    meta = {'collection': 'Categories'}


class Article(Document):
    url = fields.URLField(required=True, unique=True)
    source = fields.ReferenceField(Sources)
    title = fields.StringField()
    content = fields.StringField()
    publish_date = fields.DateTimeField()
    author = fields.StringField()
    categories = fields.ListField(fields.ReferenceField(Category))
    tag = fields.ListField(fields.ReferenceField(ArticleTag))
    meta = {'collection': 'Articles'}
