from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('/', views.article_detail)

]
# This has been significantly changed in Django 3, this could be done like this:path('/', views.article_detail),
# where the first slug "" is the name of the parameter which could be any name; "abc", "the_slug", etc.
# If you still insist on using regex then there is one thing to change; the method name instead of "url" 
# use "re_path":re_path(r'^(?P[\w-]+)/$', views.article_detail),