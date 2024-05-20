from django.db import models


class Contact(models.Model):
    """Represents each message received and saved on the database"""
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    order_number = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message {self.subject} from {self.name}."
    