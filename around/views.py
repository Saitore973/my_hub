from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm, userProfileForm, NeighbourhoodForm, BusinessForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . models import Profile, Neighborhood, Business
# Create your views here.
@login_required(login_url='login')
def welcome(request):
    return render(request, 'welcome.html')


@login_required(login_url='login')
def home(request):
    neighbours =Neighborhood.objects.all()
    form=NeighbourhoodForm(request.POST, request.FILES)
    if form.is_valid():
            name=form.cleaned_data['name']
            location=form.cleaned_data['location']
            image=form.cleaned_data['image']

            created=Neighborhood(name=name,location=location,image=image, user=request.user)
            created.save()
    return render(request, 'index.html', {'form':form, 'neighbours':neighbours})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get("username")
           
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
    form = NeighbourhoodForm()
   
    if request.method == 'POST':
        form=NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            location=form.cleaned_data['location']
            image=form.cleaned_data['image']

            created=Neighborhood(name=name,location=location,image=image, user=request.user)
            created.save()

        
    return render(request, 'all/neighbourhood.html', {'form':form, })
    
def neighbourdisplay(request):
    
    return render(request, 'all/hood.html',)

def accountSettings(request):
	Profile = request.user.profile
	form = userProfileForm(instance=Profile)

	if request.method == 'POST':
		form = userProfileForm(request.POST, request.FILES,instance=Profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
    
	return render(request, 'all/settings.html', context)


def business(request):
    neighbours =Business.objects.all()
    form=BusinessForm(request.POST, request.FILES)
    if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            description=form.cleaned_data['description']

            created=Business(name=name,email=email,description=description, user=request.user)
            created.save()
    return render(request, 'all/business.html', {'form':form, 'neighbours':neighbours})

def businessedit(request):
    form = BusinessForm()
   
    if request.method == 'POST':
        form=BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            description=form.cleaned_data['description']

            created=Business(name=name,email=email,description=description)
            created.save()

        
    return render(request, 'all/edit.html', {'form':form, })

def hoods(request):
    all_hoods = Neighborhood.objects.all()
    all_hoods = all_hoods[::-1]
    params = {
        'all_hoods': all_hoods,
    }
    return render(request, 'all_hoods.html', params)

