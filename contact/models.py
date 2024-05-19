from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    order_number = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message {self.subject} from {self.name}."
    