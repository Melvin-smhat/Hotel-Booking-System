from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from general.email_backend import Emailbackend
from .forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'general/index.html')
    else:
        messages.error(request, 'Login First ')
        return redirect(reverse('login'))
        

def about(request):
    return render(request, 'general/about.html')

def service(request):
    return render(request, 'general/services.html')

def pricing(request):
    return render(request, 'general/pricing.html')

def blog(request):
    return render(request, 'general/blog.html')

def blog_single(request):
    return render(request, 'general/blog-single.html')

def testimonials(request):
    return render(request, 'general/testimonials.html')

def register(request):
    form=RegistrationForm(request.POST or None, request.FILES or None)
    context={
        'title':'Sign Up',
        'form':form
        }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successful')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Registration Failed')
    return render(request, 'general/register.html',context)
    

def dashboard(request):
    return render(request, 'general/dashboard.html')

def log_in(request):
    context={
        'title':'Login'
    }
    if request.method=="POST":
        username = request.POST.get('username')
        password=request.POST.get('password')
        user=Emailbackend.authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)           
            return redirect('index')
        else:
            messages.error(request, 'Invalid details')
            return redirect(reverse('login'))
    else:
            return render(request, 'general/login.html', context)

def log(request):
    logout(request)
    # messages.info(request, 'logged out')
    return redirect(reverse('dashboard'))
