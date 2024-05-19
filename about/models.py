from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
