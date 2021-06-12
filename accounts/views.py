from django.contrib import messages
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from users.models import NewUser

from .models import ProjectInfo

# Create your views here.

def login(request):
    # show project name and logo in login page (data from database)
    p_info = ProjectInfo.objects.all()

    if request.method == 'POST':  # if user posted data and clicked on log in do the below
        email = request.POST['email']  # retrieve the posted data in email
        password = request.POST['password']  # retrieve the posted data in password

        user = auth.authenticate(email=email, password=password)  # check if the credentials are correct

        if user is not None:  # if the credentials are correct go to index
            auth.login(request, user)
            return redirect('index')
        else:
            # show message on login page if credentials are incorrect
            messages.info(request, 'ERROR! Invalid Credentials.')
            return render(request, 'login.html', {'p_info': p_info})
    else:
        if request.user.is_authenticated:
            return redirect('index')
        # if not go back to login page
        else:
            return render(request, 'login.html', {'p_info': p_info})  # if there are no posted data show login page


def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    p_info = ProjectInfo.objects.all()

    if request.method == 'POST': # if user posted data and clicked on sign up retrieve the below
        email = request.POST['email']
        split_string = email.split("@", 1)
        user_name = split_string[0]
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        if NewUser.objects.filter(email=email).exists():
            messages.info(request, 'ERROR! Email already Exists.')

        else:
            user = NewUser.objects.create_user(email=email, user_name=user_name, first_name=first_name, last_name=last_name, password=password, vacation_balance=5, is_active=1)
            user.save()

            # print('user created')
            messages.info(request, 'Success! User Created.')
            return redirect('/')

    return render(request, 'register.html', {'p_info': p_info})
