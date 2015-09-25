from mongoengine import *
import bcrypt
from datetime import datetime

class Token(EmbeddedDocument):
    value = StringField()
    updated_at = DateTimeField(help_text='date updated')

class User(Document):
    username = StringField(max_length=20, unique=True)
    email = StringField(unique=True)
    password = StringField()
    created_at = DateTimeField(help_text='date created')
    updated_at = DateTimeField(help_text='date updated')
    access_token = EmbeddedDocumentField(Token)

    meta = {
        'indexes' : ['username', 'email']
    }

    """
    Create new user
    """
    @classmethod
    def new(cls, data):
        try:
            user = cls(
                username     = data['username'],
                email        = data['email'],
                password     = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()),
                created_at   = datetime.now(),
                updated_at   = datetime.now(),
                access_token = {"value":"", "updated_at":""}
            )
            user.save()
            message = {"success": {
                "username"   : user.username,
                "created_at" : str(user.created_at)
            }}
        except NotUniqueError:
            # type(e).__name__
            message = {"error" : ["This username or email has been taken."]}
        except Exception as e:
            message = {"error" : [str(e)]}
        return message

    def to_json(self):
        return {
            "id"           : str(self.id),
            "username"     : self.username,
            "email"        : self.email,
            "password"     : self.password,
            "created_at"   : self.created_at,
            "updated_at"   : self.updated_at,
            "access_token" : {
                "value"      : self.access_token.value,
                "updated_at" : self.access_token.updated_at
            }
        }
