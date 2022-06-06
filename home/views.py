from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'index.html',)

def contact(request):
    return render(request, 'contact.html',)

def about(request):
    return render(request, 'about.html',)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def single(request):
    return render(request, 'single.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def signup(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect("login")
        else:
            return redirect("about")
    
    return render(request, "signup.html")

    git commit-m "update" git push -u origin master