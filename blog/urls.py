from django.conf.urls import url

from views.user import ReadUser, CreateUser, UserLogin, UserLogout
from views.blog import ReadBlog
from views.tag import ReadTag

urlpatterns = [
    url(r'^v1/user/(?P<key>.*)$', ReadUser.as_view(), name='read_user'),
    url(r'^v1/user$', CreateUser.as_view(), name='create_user'),
    url(r'^login$', UserLogin.as_view(), name='user_login'),
    url(r'^logout$', UserLogout.as_view(), name='user_logout'),
    url(r'^v1/blog/(?P<blog_id>.*)$', ReadBlog.as_view(), name='read_blog'),
    url(r'^v1/tag/(?P<tag_id>.*)$', ReadTag.as_view(), name='read_tag'),
]
