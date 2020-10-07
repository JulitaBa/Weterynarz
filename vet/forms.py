from django import forms
from .models import Message
from .models import News


class MessageForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Adres e-mail', 'size': 38}
        ),
    )
    subject = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Temat', 'size': 38}
        ),
    )
    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(
            attrs={'placeholder': 'Treść wiadomości'}
        ),
    )

    class Meta:
        model = Message
        exclude = ['created']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text',)
