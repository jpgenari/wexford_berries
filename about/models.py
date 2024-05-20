from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class AboutPage(models.Model):
    "Stores content on database to be displayed on front end"
    content = HTMLField()
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
