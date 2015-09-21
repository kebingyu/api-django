from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bson.json_util import dumps
from bson.objectid import ObjectId
import sys

from models.tag import Tag

class ReadTag(ListView):
    def get(self, request, tag_id):
        try:
            tag = Tag.objects(id = ObjectId(tag_id)).first()
            message = tag.to_json()
        except:
            message = {"error": "Tag not found"}

        return HttpResponse(dumps(message))
