from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    email = models.CharField('Email', max_length=200)
    subject = models.CharField('Tytuł', max_length=200)
    message = models.TextField('Wiadomość', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    objects = None
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.text