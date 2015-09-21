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
