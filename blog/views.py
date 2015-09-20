from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bson.json_util import dumps
from bson.objectid import ObjectId
import sys

from .models import User, Token, Blog, EmbeddedTag, Tag

class ReadUser(ListView):
    def get(self, request, key):
        try:
            user = User.objects(username = key).first()
            message = user.to_json()
        except:
            message = {"error": "User not found"}
        return HttpResponse(dumps(message))

class UserLogin(UpdateView):
    def post(self, request):
        return HttpResponse('login')

class UserLogout(DeleteView):
    def delete(self, request):
        return HttpResponse('logout')

class ReadBlog(ListView):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects(id = ObjectId(blog_id)).first()
            message = blog.to_json()
        except:
            message = {"error": "Blog not found"}
        
        return HttpResponse(dumps(message))

class ReadTag(ListView):
    def get(self, request, tag_id):
        try:
            tag = Tag.objects(id = ObjectId(tag_id)).first()
            message = tag.to_json()
        except:
            message = {"error": "Tag not found"}

        return HttpResponse(dumps(message))
