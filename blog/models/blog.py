from mongoengine import *

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
