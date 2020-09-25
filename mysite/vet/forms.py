from django.forms import ModelForm
from django import forms
from .models import Message
from .models import News


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['created']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text',)