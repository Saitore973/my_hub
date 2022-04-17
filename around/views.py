from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import NeighbourhoodForm
from . models import userProfile, Neighborhood
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get("username")
            userProfile.objects.create(
                user=user,
            )
            messages.success(request, 'Account succefuly created for'+ user)
            return redirect('login')
    context = {'form':form}
    return render (request, 'all/register.html', context)
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request, 'username OR password is incorrect')
            
    context = {}
    return render(request, 'all/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def neighborhood(request):
    Neighborhood = userProfile.objects.get(user=request.user)
    form = NeighbourhoodForm()
    mainform = CreateUserForm(instance=request.user.profile)
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            image = form.cleaned_data['image']
            created_project = Neighborhood(name=name,location=location,image=image,user=user)
            created_project.save()
            return redirect('home')
    if request.method == 'POST':
        mainform = CreateUserForm(request.POST, request.FILES, instance=request.user.profile)
        if mainform.is_valid():
            mainform.save()
            return redirect('profile')
    return render(request, 'all/user.html',{"name":"userProfile","form":form,"mainform":mainform,"userProfile":userProfile})