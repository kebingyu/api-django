from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bson.json_util import dumps
from bson.objectid import ObjectId
import sys
import json

from models.user import User, Token
from validator import Validator

class ReadUser(ListView):
    def get(self, request, key):
        try:
            user = User.objects(username = key).first()
            message = user.to_json()
        except:
            message = {"error": "User not found"}
        return HttpResponse(dumps(message))

class CreateUser(CreateView):
    def post(self, request):
        if (request.body == ''):
            data = {}
        else:
            data = json.loads(request.body)

        errors = Validator.validate(data, {
            'username' : 'required|max:20',
            'email'    : 'required|email',
            'password' : 'required|min:6|confirmed',
        })
        if (errors):
            message = {"error": errors}
        else:
            message = User.new(data)
        return HttpResponse(dumps(message))

class UserLogin(UpdateView):
    def post(self, request):
        return HttpResponse('login')

class UserLogout(DeleteView):
    def delete(self, request):
        return HttpResponse('logout')
