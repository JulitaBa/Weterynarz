from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage

from .forms import MessageForm


# Create your views here.
def vet(request):
    return render(request, 'vet/vet.html')
def onas(request):
    return render(request, 'vet/onas.html')


def sendMessage(request):
    if request.method == 'GET':
        return render(request, 'vet/contact.html', {'form': MessageForm})
    else:
        email = EmailMessage(
            request.POST['subject'],
            request.POST['message'],
            'formularz@krt29.pl',
            ['kuba.brodowski@gmail.com'],
            reply_to = [request.POST['email'],]
        )
        email.send()
        return render(request, 'vet/contact.html', {'info': 'Wiadomość wysłana!'})
