from mongoengine import *

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
