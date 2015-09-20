from mongoengine import *

class Token(EmbeddedDocument):
    value = StringField()
    updated_at = DateTimeField(help_text='date updated')

class User(Document):
    username = StringField(max_length=20)
    email = StringField()
    password = StringField()
    created_at = DateTimeField(help_text='date created')
    updated_at = DateTimeField(help_text='date updated')
    access_token = EmbeddedDocumentField(Token)

    meta = {
        'indexes' : ['username', 'email']
    }

    def to_json(self):
        return {
            "id" : str(self.id),
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
            "access_token" : {
                "value": self.access_token.value,
                "updated_at" : self.access_token.updated_at
            }
        }

class EmbeddedTag(EmbeddedDocument):
    id = ObjectIdField()
    content = StringField()

class Blog(Document):
    title = StringField()
    content = StringField()
    created_at = DateTimeField(help_text='date created')
    updated_at = DateTimeField(help_text='date updated')
    user_id = ObjectIdField()
    tags = EmbeddedDocumentListField(EmbeddedTag)

    meta = {
        'indexes' : ['user_id']
    }

    def to_json(self):
        tags = []
        for tag in self.tags:
            tags.append({
                "id" : str(tag.id),
                "content" : tag.content
            })

        return {
            "id" : str(self.id),
            "title" : self.title,
            "content" : self.content,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
            "user_id" : str(self.user_id),
            "tags" : tags
        }

class Tag(Document):
    content = StringField()
    created_at = DateTimeField(help_text='date created')
    updated_at = DateTimeField(help_text='date updated')
    user_id = ObjectIdField()
    blogs = ListField(ObjectIdField())

    meta = {
        'indexes' : ['content', 'user_id']
    }

    def to_json(self):
        blogs = []
        for id in self.blogs:
            blogs.append({
                "id" : str(id)
            })

        return {
            "id" : str(self.id),
            "content" : self.content,
            "created_at" : self.created_at,
            "updated_at" : self.updated_at,
            "user_id" : str(self.user_id),
            "blogs" : blogs
        }
