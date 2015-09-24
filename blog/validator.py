import re

class Validator(object):
    @classmethod
    def required(cls, key, value):
        msg = '';
        if len(value) == 0:
            msg = key + ' is required.'
        return msg;

    @classmethod
    def email(cls, key, value):
        msg = '';
        if not re.match(r"/^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i", value):
            msg = 'Please provide a valid email.'
        return msg;

    @classmethod
    def validate(cls, data, rules):
        message = []
        for field in rules:
            if field in data:
                value = data[field]
            else:
                value = ''
            for rule in rules[field].split('|'):
                msg = getattr(cls, rule)(field, value)  
                if len(msg) > 0:
                    message.append(msg)
        return message
