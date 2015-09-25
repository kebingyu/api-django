import re

class Validator(object):
    @classmethod
    def required(cls, key, value):
        msg = ''
        if len(value) == 0:
            msg = key + ' is required.'
        return msg

    @classmethod
    def email(cls, key, value):
        msg = ''
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            msg = 'Please provide a valid email.'
        return msg

    @classmethod
    def max(cls, key, val, length):
        msg = ''
        if val and len(val) > length:
            msg = key + ' exceeds ' + str(length) + ' characters.'
        return msg

    @classmethod
    def min(cls, key, val, length):
        msg = ''
        if val and len(val) < length:
            msg = key + ' must be longer than ' + str(length) + ' characters.'
        return msg

    @classmethod
    def confirmed(cls, key, data):
        # By default look for "key" and "key_confirmation"
        msg = ''
        if (key in data) and (key + '_confirmation' in data) and data[key] == data[key + '_confirmation']:
            msg = ''
        else:
            msg = key + ' provided do not match.'
        return msg

    @classmethod
    def validate(cls, data, rules):
        message = []
        for field in rules:
            if field in data:
                value = data[field]
            else:
                value = ''
            for rule in rules[field].split('|'):
                msg = ''
                if rule.find(':') > -1:
                    sep = rule.split(':')
                    if sep[0] == 'min' or sep[0] == 'max':
                        msg = getattr(cls, sep[0])(field, value, int(sep[1]))
                elif rule == 'confirmed':
                    msg = getattr(cls, rule)(field, data)  
                else:
                    try:
                        msg = getattr(cls, rule)(field, value)  
                    except Exception, e:
                        # invalid method name
                        print 'Error validating rule: ', str(e)
                        continue

                if len(msg) > 0:
                    message.append(msg)
                    break
        return message
