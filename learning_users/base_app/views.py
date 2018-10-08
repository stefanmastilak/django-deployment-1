from django.shortcuts import render
from base_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# ak chceme aby user musel byt prihlaseni tak pouzijeme:
from django.contrib.auth.decorators import login_required
# Create your views here.

def indexView(request):
    return render(request, 'base_app/index.html')

@login_required
def specialView(request):
    return HttpResponse('You are logged in, Nice!')

@login_required
def user_logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) # index view

def registerView(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']\

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'base_app/registration.html',
                            {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered':registered})

def user_loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username') # v login.html je to username
        password = request.POST.get('password') # v login.html je to password

        user = authenticate(username=username, password=password) # true/false

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) # index view
            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password: {}'.format(username,password))
    else:
        return render(request, 'base_app/login.html',{})
