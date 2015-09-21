from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bson.json_util import dumps
from bson.objectid import ObjectId
import sys

from models.blog import Blog, EmbeddedTag

class ReadBlog(ListView):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects(id = ObjectId(blog_id)).first()
            message = blog.to_json()
        except:
            message = {"error": "Blog not found"}
        
        return HttpResponse(dumps(message))
