from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from django.utils import timezone
from django.core.mail import send_mail
from .forms import MessageForm, NewsForm
from django.contrib import messages

# Create your views here.
def news(request):
    posts = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'vet/news.html', {'posts': posts})

def news_edit(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'vet/news_edit.html', {'post': post})

def news_add_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'vet/news_add_new.html', {'form': form})

def news_change(request, pk):
    post = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_edit', pk=post.pk)
    else:
        form = NewsForm(instance=post)
    return render(request, 'vet/news_change.html', {'form': form})

def news_delete(request, pk):
    post = get_object_or_404(News, pk=pk)
    post.delete()
    return redirect('news')


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
def contact_sent(request):
    return render(request, 'vet/contact_sent.html')


def sendMessage(request):
    if request.method == "GET":
        form = MessageForm()
    else:
        form = MessageForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, ['julita.babecka@gmail.com', email])
            messages.add_message(request, messages.SUCCESS, "Wiadomość wysłana!", fail_silently=True)
        form = MessageForm()
    return render(request, 'vet/contact.html', {'form': form})