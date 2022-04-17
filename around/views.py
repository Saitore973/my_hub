from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render (request, 'all/register.html', context)
def loginPage(request):
    context = {}
    return render(request, 'all/login.html', context)