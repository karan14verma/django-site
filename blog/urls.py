from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [url(r'^blog/^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="blog/blog.html"))]
