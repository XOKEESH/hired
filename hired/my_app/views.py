from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Good Morning!</h1>')

def application_detail(request):
    return render(request, 'application_detail.html')