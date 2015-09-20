from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^v1/user/(?P<key>.*)$', views.ReadUser.as_view(), name='read_user'),
    url(r'^login$', views.UserLogin.as_view(), name='user_login'),
    url(r'^logout$', views.UserLogout.as_view(), name='user_logout'),
    url(r'^v1/blog/(?P<blog_id>.*)$', views.ReadBlog.as_view(), name='read_blog'),
    url(r'^v1/tag/(?P<tag_id>.*)$', views.ReadTag.as_view(), name='read_tag'),
]
