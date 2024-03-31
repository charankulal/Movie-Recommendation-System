from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import  User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# from .forms import RoomForm,UserForm,MyUserCreationForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home_page.html')
def mrs_home(request):
    return render(request, 'mrs_home.html')


def loginPage(request):
    page = 'login'
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Account does not exist")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('mrs_home')
        else:
            messages.error(request, "Invalid User Credentials")

    context = {'page': page}
    return render(request, 'login_page.html', context)