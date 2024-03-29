from django.db import models
from django.db.models.fields import SlugField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'
