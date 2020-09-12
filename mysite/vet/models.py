from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.CharField('Email', max_length=200)
    subject = models.CharField('Tytuł', max_length=200)
    message = models.TextField('Wiadomość', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)