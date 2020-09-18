from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage

from .forms import MessageForm


# Create your views here.
def vet(request):
    return render(request, 'vet/vet.html')
def onas(request):
    return render(request, 'vet/onas.html')
def internistyczne(request):
    return render(request, 'vet/internistyczne.html')
def profilaktyczne(request):
    return render(request, 'vet/profilaktyczne.html')
def chirurgiczne(request):
    return render(request, 'vet/chirurgiczne.html')
def ortopedyczne(request):
    return render(request, 'vet/ortopedyczne.html')
def badania_lab(request):
    return render(request, 'vet/badania_lab.html')
def rtg_ekg(request):
    return render(request, 'vet/rtg_ekg.html')
def pielegnacja(request):
    return render(request, 'vet/pielegnacja.html')
def paszporty(request):
    return render(request, 'vet/paszporty.html')
def czipowanie(request):
    return render(request, 'vet/czipowanie.html')
def diety(request):
    return render(request, 'vet/diety.html')

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
