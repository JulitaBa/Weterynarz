from django.shortcuts import render

# Create your views here.
def vet(request):
    return render(request, 'vet/vet.html')