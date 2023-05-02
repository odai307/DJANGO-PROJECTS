from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists!")
                return redirect('signup')           
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists!")
                return redirect('signup')            
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password doesn't match!!")
            return redirect('signup')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect('login')
        auth.login(request, user)
        return redirect('home')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')