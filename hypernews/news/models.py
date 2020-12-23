from django.db import models


class Article(models.Model):

    created = models.DateTimeField()
    text = models.TextField("Text")
    title = models.CharField("Title", max_length=150)
    link = models.SlugField(max_length=160, unique=True)



